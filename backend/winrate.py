import pandas as pd
from data_clean import clean_data
import matplotlib.pyplot as pl
from main import df

df = clean_data(df)

print("[bold]Best Team by Winrate[/bold]")

home_teams =  df[["HomeTeam","FTR"]].copy() #best team which has best winning rate
clean_data(home_teams)
home_teams["result"]=home_teams["FTR"].map({'H':'W','D':'D','A':'L'})
home_teams.rename(columns={"HomeTeam":"Team"},inplace=True)

away_teams =  df[["AwayTeam","FTR"]].copy()
clean_data(away_teams)
away_teams["result"]=away_teams["FTR"].map({'H':'L','D':'D','A':'W'})
away_teams=away_teams.rename(columns={"AwayTeam":"Team"},inplace=True)

all_teams = pd.concat([home_teams,away_teams])
win=all_teams[all_teams['result']=="W"] ['Team'].value_counts()
matches=all_teams['Team'].value_counts()


winrate=(win/matches).sort_values(ascending=False)
print(round(winrate,2))
sort4=winrate
top_t4=sort4.index[0]

print(f"[bold cyan]{top_t4}  is the Team scored most Winrate . We can see as Thier result going. [/bold cyan]")

sort4.plot(kind="bar")
pl.title("Best Team By  winning rate")
pl.xlabel("Team")
pl.ylabel("WinRate")
pl.plot()
pl.show()