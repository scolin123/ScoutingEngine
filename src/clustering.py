import pandas as pd
from sklearn.cluster import KMeans
from src.data_loader import load_data
from src.preprocess import clean_data

def analyze_tunneling():
    df = clean_data(load_data())

    X = df[['x','y']]

    kmeans = KMeans(n_clusters=5,random_state=42,n_init='auto')
    df['cluster'] = kmeans.fit_predict(X)

    tunneling_stats = df.groupby(['pitcher_name','cluster'])['pitch_type'].nunique()

    print("---Tunneling Analysis (Deception Score)---")
    print(tunneling_stats)

if __name__ == "__main__":
    analyze_tunneling()