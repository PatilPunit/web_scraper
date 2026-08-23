import pandas as pd

def clean_data(df:pd.DataFrame)-> pd.DataFrame:
    """
    Cleans the data by removing duplicates and handling missing values.
    
    """
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.fillna(0, inplace=True)
    return df