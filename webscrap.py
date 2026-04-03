import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as pl
 #selection function
def select():
   l=[17,18,19,20,21,22,23] #kist of years
   event = ['E0','E1','E2','E3','EC'] #list of events
   print("Choose the year for csv file between:")
   for i in l : print(i,i+1)            #loop of years
   year = input("Choose : ")

   print("Choose the event for csv file between:")
   for i in event : print(i)             #loop of events
   event_select= input("Choose : ")
   link = "https://www.football-data.co.uk/mmz4281/" + year+"/"+event_select+"."+"csv"  #link which acces and bring the data
   df=pd.read_csv(link)
   print(df)

   run =True
  
   while run == True :
        print("1.Show Best Home Team")
        print("1.Show Best Away Team")
        print("3.Show Best Team by Result")
        print("4.Show Best Team by Winrate")
        print("5.Show Best Team By Goals")
        print("Best Goal scoring teams")
        n = int(input("Enter your choice :"))
       
        if n==1 :
          print("show top home teams of full time ")   #showing the home team has best score at full time
          home_goals=df[["HomeTeam","FTHG"]].copy()
          home_goals.rename(columns={"FTHG":"Goals"},inplace=True)
          home_stats=home_goals.groupby("HomeTeam")  ["Goals"].sum()
          
          # home_goals["Goals"] = home_team.groupby("HomeTeam") ["FTHG"].value_counts().unstack(fill_value=0)
          print(home_stats.sort_values(ascending=False))
          sort=home_stats.sort_values(ascending=False)
          
          sort.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Goals scord by Teams")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
        elif n==2:
          print("show top away teams of full time")   #showing the away team has best score at full time 
         
          away_goals=df[["AwayTeam","FTAG"]].copy()
          away_goals.rename(columns={"FTAG":"Goals"},inplace=True)
        

          away_stats=away_goals.groupby("AwayTeam")  ["Goals"].sum()
          print(away_stats.sort_values(ascending=False))
          sort2=away_stats.sort_values(ascending=False)
          sort2.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Goals scord by Teams")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
          
          # away_goals = df.groupby("AwayTeam") ["FTAG"].max()
         
        elif n ==3:
          home_team =  df[["HomeTeam","FTR"]].copy()  #best team and thier results
          home_team["result"]=home_team["FTR"].map({'H':'W','D':'D','A':'L'})
          home_team.rename(columns={"HomeTeam":"Team"},inplace=True)

          away_team =  df[["AwayTeam","FTR"]].copy()
          away_team["result"]=away_team["FTR"].map({'H':'W','D':'D','A':'L'})
          away_team=away_team.rename(columns={"AwayTeam":"Team"},inplace=True)
 
          all_team = pd.concat([home_team,away_team])
          team_stats= all_team.groupby("Team") ["result"].value_counts().unstack(fill_value=0)
          print(team_stats.sort_values(ascending=False,by="W"))
          sort3=team_stats.sort_values(ascending=False,by="W")
          sort3.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Best team  by result")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
          
        elif n == 4:
          home_teams =  df[["HomeTeam","FTR"]].copy() #best team which has best winning rate
          home_teams["result"]=home_teams["FTR"].map({'H':'W','D':'D','A':'L'})
          home_teams.rename(columns={"HomeTeam":"Team"},inplace=True)

          away_teams =  df[["AwayTeam","FTR"]].copy()
          away_teams["result"]=away_teams["FTR"].map({'H':'W','D':'D','A':'L'})
          away_teams=away_teams.rename(columns={"AwayTeam":"Team"},inplace=True)
 
          all_teams = pd.concat([home_teams,away_teams])
          win=all_teams[all_teams['result']=="W"] ['Team'].value_counts()
          matches=all_teams['Team'].value_counts()

          winrate=(win/matches).sort_values(ascending=False)
          print(round(winrate,2))
          sort4=winrate
          sort4.plot(kind="bar")
          pl.title("Best Team By  winning rate")
          pl.xlabel("")
          pl.ylabel("")
          pl.plot()
          pl.show()

        elif n == 5  : 
          home_g = df[["HomeTeam","FTHG"]].copy() #best away and home team by goals
          home_g= home_g.rename(columns={'FTHG':'Goal',"HomeTeam":"Team"})
          home_g=home_g.groupby('Team') ['Goal'].sum()

          away_g = df[["AwayTeam","FTAG"]].copy()
          away_g = away_g.rename(columns={'FTAG':'Goal',"AwayTeam":"Team"})
          
          away_g=away_g.groupby('Team') ['Goal'].sum()


          all_g=pd.concat([away_g,home_g])
          # all_g = all_g.groupby('Team') ['Goal'].sum()
          print(all_g.sort_values(ascending=False))
          sort5=all_g.sort_values(ascending=False)

          sort5.plot(kind="bar")
          pl.title("Best Team By Goals")
          pl.xlabel("")
          pl.ylabel("")
          pl.plot()
          pl.show()
        elif 6 :
           
           hs_team = df[["HS","HomeTeam","FTHG"]].copy()
           hs_team.rename(columns={"HS":"TeamShots","HomeTeam":"Team","FTHG":"Goals"},inplace=True)
           hs_team = hs_team.groupby("Team") [['TeamShots','Goals']].sum()
           print(hs_team)
           as_team = df[["AS","AwayTeam","FTAG"]].copy()
           as_team.rename(columns={"AS":"TeamShots","AwayTeam":"Team","FTAG":"Goals"},inplace=True)
           as_team = as_team.groupby("Team") [['TeamShots','Goals']].sum()
           print(as_team)

           ts_team = pd.concat([hs_team,as_team])
           shotrate = pd.concat([hs_team,as_team])
           ts_team.groupby("Team") [["Goals","TeamShots"]].value_counts()
           
           total_shots=ts_team['TeamShots'].value_counts()
           total_goals=ts_team['Goals'].value_counts()
           shotrate = (total_goals/total_shots).sort_values(ascending=False)
           round(shotrate,2)
           shotrate.groupby('Team')
          #  print(round(shotrate,2))
           sort6=shotrate
           sort6.plot(kind="bar")
           pl.title("Best Team By Goals")
           pl.xlabel("")
           pl.ylabel("")
           pl.plot()
           pl.show()


           
                   
def main():
    run =True
  
    while run == True :
        print("1.Select The Year and event ")
        
        n = int(input("Enter your choice :"))
        if n == 1:
           select()
        
main()
          
     
    