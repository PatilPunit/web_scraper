import pandas as pd
from data_clean import clean_data
import matplotlib.pyplot as pl
from main import df

df = clean_data(df)

print("[bold]Show Best defending Team[/bold]")

hd_team=df[["FTAG","HomeTeam"]].copy() 
clean_data(hd_team)
hd_team.columns=["Goals","Team"]
hd_df=hd_team.groupby("Team") ["Goals"].sum()
print(hd_df)

ad_team=df[["FTHG","AwayTeam"]].copy()
clean_data(ad_team)
ad_team.columns=["Goals","Team"]
ad_df=ad_team.groupby("Team") ["Goals"].sum()
print(ad_df)

all_d=pd.concat([ad_team,hd_team])
def_team=all_d.groupby("Team") ["Goals"].sum()

sort7=def_team.sort_values(ascending=False)
print(sort7)
top_t7=sort7.index[0]
print(f"[bold cyan]{top_t7}  is the Team is a Shield . Even if the front of best attack this kept thier arena safe. [/bold cyan]")

sort7.plot(kind="bar")
pl.title("Best Defensive Team ")
pl.xlabel("Team")
pl.ylabel("DefenseRate")
pl.plot()
pl.show()
