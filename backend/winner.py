import pandas as pd
from data_clean import clean_data
import matplotlib.pyplot as pl
from main import df

df = clean_data(df)

teams = sorted(df['HomeTeam'].unique())
for i ,team in enumerate(teams,1):
   print(f"{i}.{team}")

chioce= int(input("Enter the team number : "))
teamnum= teams[chioce-1]
team_df = df[(df["HomeTeam"]==teamnum) | (df['AwayTeam']==teamnum)]

h_goals = team_df[team_df['HomeTeam']==teamnum] ['FTHG'].sum()
a_goals = team_df[team_df["AwayTeam"]==teamnum] ['FTAG'].sum()
t_goals = a_goals + h_goals

h_shot = team_df[team_df['HomeTeam']==teamnum] ['HS'].sum()
t_shotrate = h_goals   / h_shot      

wins = len(team_df[
 ((team_df['HomeTeam'] == teamnum) & (team_df['FTR'] == 'H')) |
 ((team_df['AwayTeam'] == teamnum) & (team_df['FTR'] == 'A'))])

matchw= len(team_df)
winr=wins/matchw

h_def = team_df[team_df['HomeTeam']==teamnum] ['FTAG'].sum()

h_win=len(team_df[
 ((team_df['HomeTeam'] == teamnum) & (team_df['FTR'] == 'H'))])
h_lose=len(team_df[
 ((team_df['HomeTeam'] == teamnum) & (team_df['FTR'] == 'A'))])
h_draw=len(team_df[
   ((team_df['HomeTeam']==teamnum ) & (team_df['FTR']=='D'))])



print("------------------------------------------------------------------")
print("Team : ",teamnum)
print("Total Goals : ",t_goals)
print("Winrate : ",round(winr,2))
print("Shotrate : ",round(t_shotrate,2))
print("Taken Goals : ",h_def)

print("Total Wins : ", h_win)
print("Total lose : ",h_lose)
print("Total Draws : ",h_draw)
print("------------------------------------------------------------------")
