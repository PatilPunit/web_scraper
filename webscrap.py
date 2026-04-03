import pandas as pd
import numpy as np 
import math
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
        n = int(input("Enter your choice :"))
       
        if n==1 :
          print("show top home teams of full time ")   #showing the home team has best score at full time
          home_goals=df[["HomeTeam","FTHG"]].copy()
          home_goals.rename(columns={"FTHG":"Goals"},inplace=True)
          home_stats=home_goals.groupby("HomeTeam")  ["Goals"].sum()
          
          # home_goals["Goals"] = home_team.groupby("HomeTeam") ["FTHG"].value_counts().unstack(fill_value=0)
          print(home_stats.sort_values(ascending=False))
          
        elif n==2:
          print("show top away teams of full time")   #showing the away team has best score at full time 
         
          away_goals=df[["AwayTeam","FTAG"]].copy()
          away_goals.rename(columns={"FTAG":"Goals"},inplace=True)
        

          away_stats=away_goals.groupby("AwayTeam")  ["Goals"].sum()
          print(away_stats.sort_values(ascending=False))
          
          # away_goals = df.groupby("AwayTeam") ["FTAG"].max()
         
        elif n ==3:
          home_team =  df[["HomeTeam","FTR"]].copy()  #best team and thier results
          home_team["result"]=home_team["FTR"].map({'H':'W','D':'D','A':'L'})
          home_team.rename(columns={"HomeTeam":"Team"},inplace=True)

          away_team =  df[["AwayTeam","FTR"]].copy()
          away_team["result"]=away_team["FTR"].map({'H':'W','D':'D','A':'L'})
          away_team=away_team.rename(columns={"AwayTeam":"Team"},inplace=True)
 
          all_team = pd.concat([home_team,away_team])
          team_stats= all_team.groupby("Team") ["result"].value_counts().unstack(fill_value=0).head()
          print(team_stats.sort_values(ascending=False,by="W"))
        
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
                   
def main():
    run =True
  
    while run == True :
        print("1.Select The Year and event ")
        
        n = int(input("Enter your choice :"))
        if n == 1:
           select()
        
main()
          
     
    