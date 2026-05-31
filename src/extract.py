import pandas as pd

def extract_csv(filepath,columns = None):
    try:
        df= pd.read_csv(filepath)
        if columns:
            df = df[columns]
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

        