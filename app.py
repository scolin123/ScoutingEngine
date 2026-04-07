import streamlit as st
from src.data_loader import load_data
from src.preprocess import clean_data
import matplotlib.patches as patches
import matplotlib.pyplot as plt

st.title("Guelph Royals Scouting Dashboard")

# 1. Load and Clean
df = clean_data(load_data())

# 2. Filter by Pitcher (Example of an EDA feature)
pitcher = st.selectbox("Select Pitcher", df['pitcher_name'].unique())
filtered_df = df[df['pitcher_name'] == pitcher]

# 3. Simple EDA Visualization
fig, ax = plt.subplots(figsize=(5,6))

strike_zone = patches.Rectangle((-0.85, 1.5), 1.7, 2.0, 
                                linewidth=2, edgecolor='black', 
                                facecolor='none', linestyle='--')

ax.add_patch(strike_zone)



ax.scatter(filtered_df['x'], filtered_df['y'], c='blue', alpha=0.5)

ax.set_xlim(-2,2)
ax.set_ylim(0,5)
ax.set_aspect('equal')
ax.set_title(f"Pitch Locations for {pitcher}")
ax.set_xlabel("Horizontal Location(ft)")
ax.set_ylabel("Vertical Height(ft)")

st.pyplot(fig)