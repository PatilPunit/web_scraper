import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as pl
from rich.console import Console
from rich.table import Table 
import  emoji
from rich import print
from rich.progress import track 
import time 

 #selection function
def select():
   l=[17,18,19,20,21,22,23] #kist of years
   event = ['E0','E1','E2','E3','EC'] #list of events
   print("Choose the year for csv file eg.(1718):")
   for i in l : print(i,i+1)            #loop of years
   year = input("Choose : ")

   print("Choose the event for csv file between eg.(E1):")
   for i in event : print(i)             #loop of events
   event_select= input("Choose : ")
   link = "https://www.football-data.co.uk/mmz4281/" + year+"/"+event_select+"."+"csv"  #link which acces and bring the data

   df=pd.read_csv(link)
   for i in track(range(20),description="Analysing Data"): time.sleep(0.1)
   print(df)

   run =True
  
   while run == True :
        show_menu()
        
        n = int(input("Enter your choice :"))
        

       
        if n==1 :
          print("[bold]show top home teams of full time [/bold]")   #showing the home team has best score at full time
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
          print("[bold]show top away teams of full time[/bold]")   #showing the away team has best score at full time 
         
          away_goals=df[["AwayTeam","FTAG"]].copy()
          away_goals.rename(columns={"FTAG":"Goals"},inplace=True)
        

          away_stats=away_goals.groupby("AwayTeam")  ["Goals"].sum()
          print(away_stats.sort_values(ascending=False))
          sort2=away_stats.sort_values(ascending=False)
          sort2.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Goals scored by Teams")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
          
          # away_goals = df.groupby("AwayTeam") ["FTAG"].max()
         
        elif n ==3:
          print("[bold]Best Team by Result[/bold]")
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
          print("[bold]Best Team by Winrate[/bold]")
          home_teams =  df[["HomeTeam","FTR"]].copy() #best team which has best winning rate
          home_teams["result"]=home_teams["FTR"].map({'H':'W','D':'D','A':'L'})
          home_teams.rename(columns={"HomeTeam":"Team"},inplace=True)

          away_teams =  df[["AwayTeam","FTR"]].copy()
          away_teams["result"]=away_teams["FTR"].map({'H':'L','D':'D','A':'W'})
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
          print("[bold]Best Team by Goals[/bold]")
          home_g = df[["HomeTeam","FTHG"]].copy() #best away and home team by goals
          home_g= home_g.rename(columns={'FTHG':'Goal',"HomeTeam":"Team"})
          home_g=home_g.groupby('Team') ['Goal'].sum()

          away_g = df[["AwayTeam","FTAG"]].copy()
          away_g = away_g.rename(columns={'FTAG':'Goal',"AwayTeam":"Team"})
          
          away_g=away_g.groupby('Team') ['Goal'].sum()
         


          all_g=pd.concat([away_g,home_g])
          
          print(all_g.sort_values(ascending=False))
          sort5=all_g.sort_values(ascending=False)

          sort5.plot(kind="bar")
          pl.title("Best Team By Goals")
          pl.xlabel("")
          pl.ylabel("")
          pl.plot()
          pl.show()
          def most_goals():
             return all_g
        elif n == 6 :
           print("[bold]Best Team by Shotrate[/bold]")
           hs_team = df[["HS","HomeTeam","FTHG"]].copy()
           hs_team.rename(columns={"HS":"TeamShots","HomeTeam":"Team","FTHG":"Goals"},inplace=True)
           hs_sr = hs_team.groupby("Team").sum()
           hs_sr['Home_ShotRate']=hs_sr['Goals']/hs_sr['TeamShots']
           sort6b=hs_sr
           print(sort6b)
           as_team = df[["AS","AwayTeam","FTAG"]].copy()
           as_team.rename(columns={"AS":"TeamShots","AwayTeam":"Team","FTAG":"Goals"},inplace=True)
           as_sr = as_team.groupby("Team").sum()
           as_sr["Away_Shotrate"]=as_sr['Goals']/as_sr['TeamShots']
           sort6a=as_sr
           print(sort6a)

           ts_team = pd.concat([hs_team,as_team])
           all_st=ts_team.groupby("Team").sum()
           all_st['shotrate']=all_st['Goals']/all_st['TeamShots']
        
           sort6=all_st["shotrate"]
           print(sort6)
           sort6.plot(kind="bar")
           pl.title("Best Team By Goals")
           pl.xlabel("")
           pl.ylabel("")
           pl.plot()
           pl.show()

        elif n == 7 :
           print(emoji.emojize(":Shield:"),"[bold]Show Best defending Team[/bold]")
           hd_team=df[["FTAG","HomeTeam"]].copy() 
           hd_team.columns=["Goals","Team"]
           hd_df=hd_team.groupby("Team") ["Goals"].sum()
          
           print(hd_df)


           ad_team=df[["FTHG","AwayTeam"]].copy()
           ad_team.columns=["Goals","Team"]
           ad_df=ad_team.groupby("Team") ["Goals"].sum()
          
          
       
           print(ad_df)

           all_d=pd.concat([ad_team,hd_team])
           def_team=all_d.groupby("Team") ["Goals"].sum()
           
           sort7=def_team.sort_values(ascending=True)
           print(sort7)
           sort7.plot(kind="bar")
           pl.title("Best Team By Goals")
           pl.xlabel("")
           pl.ylabel("")
           pl.plot()
           pl.show()

        elif n == 8 :
           win_h=df[['FTR','HomeTeam']].copy()
           win_h.columns=['Result','Team']
           win_h['Result']=win_h['Result'].map({'H':'W','D':'D','A':'L'})

           win_a=df[['FTR','AwayTeam']].copy()
           win_a.columns=['Result','Team']
           win_a["Result"]=win_a['Result'].map({'H':'L','D':'D','A':'W'})

           all_win=pd.concat([win_a,win_h])
           total_m=all_win['Team'].value_counts()
           total_w=all_win[all_win["Result"]=="W"] ['Team'].value_counts()
           winR = (total_w/total_m).sort_values(ascending=False)

           

           
          

           goal_h=df[["FTHG","HomeTeam"]].copy()
           goal_h.columns=["Goal","Team"]
           goal_h=goal_h.groupby("Team") ['Goal'].sum()

           goal_a=df[["FTAG","HomeTeam"]].copy()
           goal_a.columns=["Goal","Team"]
           
           goal_a=goal_a.groupby("Team") ['Goal'].sum()

           total_g=pd.concat([goal_a,goal_h])
           team_g= total_g.sort_values(ascending=False)

           print(team_g)
           print(round(winR,2) )

           if team_g["Team"].head(1).eqauls(winR["Team"].head(1)) :
              pass





           


          

        











def show_menu():
   console = Console()
   table = Table(title=emoji.emojize(":Soccer: Football Analyzer"),title_justify='center')
   table.add_column("Option",justify="center")
   table.add_column("Action",justify="center")

   table.add_row("1","Show Best Home Team")
   table.add_row("2","Show Best Away Team")
   table.add_row("3","Show Best Team by Result")
   table.add_row("4","Show Best Team by Goals")
   table.add_row("5","Show Best Team by Winrate")
   table.add_row("6","Show Best Attacking Team")
   table.add_row("7","Show Best Defending Team")

   console.print(table)
  
           
                   
def main():
    run =True
  
    while run == True :
        console = Console()
        print(emoji.emojize(":Soccer:"),"[bold blue]Welcome to Football Analyzer[/bold blue]")
        table = Table(title=emoji.emojize(":Soccer: Football Analyzer"),title_justify='center')
        table.add_column("Option",justify="center")
        table.add_row("1","Start")
        console.print(table)
        n = int(input("Enter your choice :"))


        if n == 1:
           select()
        
main()
          
          
     
    