import pandas as pd
from data_clean import clean_data
import matplotlib.pyplot as pl
from main import  df

df = clean_data(df)
print("[bold]Best Team by Result[/bold]")

home_team =  df[["HomeTeam","FTR"]].copy()  #best team and thier results
clean_data(home_team)
home_team["result"]=home_team["FTR"].map({'H':'W','D':'D','A':'L'}) #maping results
home_team.rename(columns={"HomeTeam":"Team"},inplace=True)

away_team =  df[["AwayTeam","FTR"]].copy()
clean_data(away_team)
away_team["result"]=away_team["FTR"].map({'H':'L','D':'D','A':'W'})
away_team=away_team.rename(columns={"AwayTeam":"Team"},inplace=True)

all_team = pd.concat([home_team,away_team])
team_stats= all_team.groupby("Team") ["result"].value_counts().unstack(fill_value=0)

print(team_stats.sort_values(ascending=False,by="W"))
sort3=team_stats.sort_values(ascending=False,by="W")
top_t3=sort3.index[0]
print(f"[bold cyan]{top_t3}  is the Team WIth most W . We can analyse thier result in their position , fisnishing at 1 . [/bold cyan]")

sort3.plot(kind="bar")
pl.xlabel("Teams")
pl.ylabel("Result")
pl.title("Best Team  by Result")
pl.xticks(rotation=90)
pl.plot()
pl.show()
