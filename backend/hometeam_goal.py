import pandas as pd
from webscrap import df
from data_clean import clean_data

cleaned_df = clean_data(df)
print(cleaned_df.head())