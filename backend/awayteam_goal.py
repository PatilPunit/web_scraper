import pandas as pd
import matplotlib.pyplot as pl
from data_clean import clean_data
from main import df

df = clean_data(df)
print("[bold]show top away teams of full time[/bold]")   #showing the away team has best score at full time 

away_goals=df[["AwayTeam","FTAG"]].copy()
clean_data(away_goals)
away_goals.rename(columns={"FTAG":"Goals"},inplace=True)
away_stats=away_goals.groupby("AwayTeam")  ["Goals"].sum()

print(away_stats.sort_values(ascending=False))
sort2=away_stats.sort_values(ascending=False)
top_t2=sort2.index[0]
print(f"[bold cyan]{top_t2}  is the Consistent in Away Games . [/bold cyan]")


sort2.plot(kind="bar")
pl.xlabel("Teams")
pl.ylabel("Goals")
pl.title("Goals scored by Away Teams")
pl.xticks(rotation=90)
pl.plot()
pl.show()