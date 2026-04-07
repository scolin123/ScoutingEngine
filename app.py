import streamlit as st
from src.data_loader import load_data
from src.preprocess import clean_data
import matplotlib.pyplot as plt

st.title("Guelph Royals Scouting Dashboard")

# 1. Load and Clean
df = clean_data(load_data())

# 2. Filter by Pitcher (Example of an EDA feature)
pitcher = st.selectbox("Select Pitcher", df['pitcher_name'].unique())
filtered_df = df[df['pitcher_name'] == pitcher]

# 3. Simple EDA Visualization
fig, ax = plt.subplots()
ax.scatter(filtered_df['x'], filtered_df['y'], c='blue', alpha=0.5)
ax.set_title(f"Pitch Locations for {pitcher}")
st.pyplot(fig)