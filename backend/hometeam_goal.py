import pandas as pd
from data_clean import clean_data
from main import df
import matplotlib.pyplot as pl
cleaned_df = clean_data(df)
print(cleaned_df.head())

print("[bold]show top home teams of full time [/bold]")   #showing the home team has best score at full time




home_goals=df[["HomeTeam","FTHG"]].copy()
clean_data(home_goals) 
home_goals.rename(columns={"FTHG":"Goals"},inplace=True)
home_stats=home_goals.groupby("HomeTeam")  ["Goals"].sum()

print(home_stats.sort_values(ascending=False))
sort=home_stats.sort_values(ascending=False)
top_team=sort.index[0]
print(f"[bold cyan]{top_team} is the Most Consistent in Home . [/bold cyan]")

sort.plot(kind="bar")
pl.xlabel("Teams")
pl.ylabel("Goals")
pl.title("Goals scord by Home Teams")
pl.xticks(rotation=90)
pl.plot()
pl.show()
