import os
import pandas as pd
import requests
from dotenv import load_dotenv
from src.preprocess import clean_data

load_dotenv()

SHEET_ID = os.getenv("GOOGLE_SHEETS_ID")
API_KEY = os.getenv("GOOGLE_SHEETS_API")

def load_data(sheet_name="Sheet1"):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{sheet_name}?key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    rows=data.get("values",[])

    if not rows:
        raise ValueError("No data found in sheet.")
    
    df = pd.DataFrame(rows[1:],columns=rows[0])

    return df


if __name__ == "__main__":
    df_raw = load_data() 
    
    df_cleaned = clean_data(df_raw) 
    
    print(df_cleaned.info())
    print(df_cleaned.head())
    
