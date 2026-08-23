import  pandas  as pd
import matplotlib.pyplot as pl
from data_clean import clean_data
from main import df

print("[bold]Best Team by Goals[/bold]")

home_g = df[["HomeTeam","FTHG"]].copy() #best away and home team by goals
clean_data(home_g)
home_g= home_g.rename(columns={'FTHG':'Goal',"HomeTeam":"Team"})
home_g=home_g.groupby('Team') ['Goal'].sum()

away_g = df[["AwayTeam","FTAG"]].copy()
clean_data(away_g)
away_g = away_g.rename(columns={'FTAG':'Goal',"AwayTeam":"Team"})
away_g=away_g.groupby('Team') ['Goal'].sum()



all_g=pd.concat([away_g,home_g])
print(all_g.sort_values(ascending=False))
sort5=all_g.sort_values(ascending=False)
top_t5=sort5.index[0]
print(f"[bold cyan]{top_t5}  is the Team scored most Goals. We can thier result as the champion. This Team is consistent in Home as well as Away matches . [/bold cyan]")

sort5.plot(kind="bar")
pl.title("Best Team By Goals")
pl.xlabel("Teams")
pl.ylabel("Goals")
pl.plot()
pl.show()