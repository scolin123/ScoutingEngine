import streamlit as st
import pandas as pd
import pickle
import numpy as np
from src.data_loader import load_data
from src.preprocess import clean_data
import matplotlib.patches as patches
import matplotlib.pyplot as plt

st.title("Guelph Royals Scouting Dashboard")

# 1. Load and Clean
df = clean_data(load_data())

with open('models/whiff_model.pkl','rb') as f:
    model = pickle.load(f)

# 2. Filter by Pitcher (Example of an EDA feature)
pitcher = st.selectbox("Select Pitcher", df['pitcher_name'].unique())
pitch_type = st.selectbox("Select Pitch type for heatmap",['FB','CV','SL','CH','SI','FC'])
filtered_df = df[df['pitcher_name'] == pitcher]

x_range = np.linspace(-2,2,50)
y_range = np.linspace(0,5,50)
xx,yy, = np.meshgrid(x_range,y_range)

grid_df = pd.DataFrame({'x':xx.ravel(),'y':yy.ravel()})

for col in model.feature_names_in_:
    if col.startswith('type'):
        grid_df[col] = 1 if col == f'type_{ pitch_type}' else 0

#predict probabilities
probs = model.predict_proba(grid_df[model.feature_names_in_])[:,1].reshape(xx.shape)

# 3. Simple EDA Visualization
fig, ax = plt.subplots(figsize=(5,6))

#Draw heatmap
contour = ax.contourf(xx,yy,probs, levels=20,cmap='Reds',alpha=0.5)
plt.colorbar(contour,label="Whiff Probability")


#Draw strikezone
strike_zone = patches.Rectangle((-0.85, 1.5), 1.7, 2.0, 
                                linewidth=2, edgecolor='black', 
                                facecolor='none', linestyle='--')

ax.add_patch(strike_zone)



ax.scatter(filtered_df['x'], filtered_df['y'], c='blue', edgecolors='white',alpha=0.6,label='Actual Pitches')

ax.set_xlim(-2,2)
ax.set_ylim(0,5)
ax.set_aspect('equal')
ax.set_title(f"Pitch Locations for {pitcher}")
ax.set_xlabel("Horizontal Location(ft)")
ax.set_ylabel("Vertical Height(ft)")

st.pyplot(fig)