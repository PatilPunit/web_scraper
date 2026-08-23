import pandas  as pd
import matplotlib.pyplot as pl
from data_clean import clean_data
from main import df

print("[bold]Best Team by Shotrate[/bold]")

hs_team = df[["HS","HomeTeam","FTHG"]].copy() #Best team which has shotrate
clean_data(hs_team)
hs_team.rename(columns={"HS":"TeamShots","HomeTeam":"Team","FTHG":"Goals"},inplace=True)
hs_sr = hs_team.groupby("Team").sum()
hs_sr['Home_ShotRate']=hs_sr['Goals']/hs_sr['TeamShots']

sort6b=hs_sr
print(sort6b)

as_team = df[["AS","AwayTeam","FTAG"]].copy()
clean_data(as_team)
as_team.rename(columns={"AS":"TeamShots","AwayTeam":"Team","FTAG":"Goals"},inplace=True)
as_sr = as_team.groupby("Team").sum()
as_sr["Away_Shotrate"]=as_sr['Goals']/as_sr['TeamShots']

sort6a=as_sr
print(sort6a)

ts_team = pd.concat([hs_team,as_team])
all_st=ts_team.groupby("Team").sum()
all_st['shotrate']=all_st['Goals']/all_st['TeamShots']

sort6=all_st["shotrate"].sort_values(ascending=False)
print(sort6)
top_t6=sort6.index[0]
print(f"[bold cyan]{top_t6}  is the Team wiht most Shotrate . They approach  as fire . Striking opponents defense [/bold cyan]")

sort6.plot(kind="bar")
pl.title("Best Team By Shotrate")
pl.xlabel("Teams")
pl.ylabel("ShotRate")
pl.plot()
pl.show()