import pandas as pd

REQUIRED_COLUMNS = [
    "game_id","date","pitcher_name","pitcher_hand",
    "batter_name","batter_hand","inning","pitch_number",
    "pitch_type","x","y","result","balls","strikes"
]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Make sure required columns exist
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns{missing_cols}")
    
    #Drop completed empty rows
    df = df.dropna(how="all")

    #Strip whitespace
    df = df.apply(lambda col:col.str.strip() if col.dtype == "object" else col)
    
    #Convert numeric columns
    df["x"] = pd.to_numeric(df["x"], errors="coerce")
    df["y"] = pd.to_numeric(df["y"], errors="coerce")
    df["balls"] = pd.to_numeric(df["balls"], errors="coerce")
    df["strikes"] = pd.to_numeric(df["strikes"], errors="coerce")
    df["inning"] = pd.to_numeric(df["inning"], errors="coerce")
    df["pitch_number"] = pd.to_numeric(df["pitch_number"], errors="coerce")

    df = df.dropna(subset=["pitch_type","x","y","result"])

    #Normalize text columns
    df["result"] = df["result"].str.lower()
    df["pitch_type"] = df["pitch_type"].str.upper()

    return df
    


