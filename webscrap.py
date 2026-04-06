#All Libraries
import pandas as pd #panda for dat handlind and dataframing 
import numpy as np #For Handling nan value
# import math
import matplotlib.pyplot as pl #For data visualization
from rich.console import Console # For printing console
from rich.table import Table #for creating table
import  emoji #for emojis
from rich import print #for crafting font 
from rich.progress import track #for animation
import time #tacking time

#selection function
def select():
   l=[17,18,19,20,21,22,23]    #list of years
   event = ['E0','E1','E2','E3','EC']   #list of events

   print("[bold]Choose the year for csv file eg.(1718):[/bold]")
   for i in l : print(i,i+1)            #loop of years
   year = input("Choose : ")

   print("[bold]Choose the event for csv file between eg.(E1):[/bold]")
   for i in event : print(i)             #loop of events
   event_select= input("Choose : ")

   link = "https://www.football-data.co.uk/mmz4281/" + year+"/"+event_select+"."+"csv"  #link which acces and bring the data

   df=pd.read_csv(link) #reading csv file

   for i in track(range(20),description="Analysing Data"): time.sleep(0.1) #that loading bar animation
   print(df)

   run =True
   while run == True :      #main loop for select
        show_menu() #That input table of features
        
        n = int(input("Enter your choice :"))
        if n==1 :
          print(emoji.emojize(":house:"),"[bold]show top home teams of full time [/bold]")   #showing the home team has best score at full time

          home_goals=df[["HomeTeam","FTHG"]].copy()  
          home_goals.rename(columns={"FTHG":"Goals"},inplace=True)
          home_stats=home_goals.groupby("HomeTeam")  ["Goals"].sum()
          
          print(home_stats.sort_values(ascending=False))
          sort=home_stats.sort_values(ascending=False)
          top_team=sort.index[0]
          print(f"[bold cyan]{top_team} is the Most Consistent in Home . [/bold cyan]",emoji.emojize(":House:"))
          
          sort.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Goals scord by Home Teams")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
        elif n==2:
          print(emoji.emojize(":stadium:"),"[bold]show top away teams of full time[/bold]")   #showing the away team has best score at full time 

          away_goals=df[["AwayTeam","FTAG"]].copy()
          away_goals.rename(columns={"FTAG":"Goals"},inplace=True)
          away_stats=away_goals.groupby("AwayTeam")  ["Goals"].sum()
          
          print(away_stats.sort_values(ascending=False))
          sort2=away_stats.sort_values(ascending=False)
          top_t2=sort2.index[0]
          print(f"[bold cyan]{top_t2}  is the Consistent in Away Games . [/bold cyan]",emoji.emojize(":Stadium:"))
          

          sort2.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.title("Goals scored by Away Teams")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
           
        elif n ==3:
          print(emoji.emojize(":rocket:"),"[bold]Best Team by Result[/bold]")

          home_team =  df[["HomeTeam","FTR"]].copy()  #best team and thier results
          home_team["result"]=home_team["FTR"].map({'H':'W','D':'D','A':'L'}) #maping results
          home_team.rename(columns={"HomeTeam":"Team"},inplace=True)

          away_team =  df[["AwayTeam","FTR"]].copy()
          away_team["result"]=away_team["FTR"].map({'H':'W','D':'D','A':'L'})
          away_team=away_team.rename(columns={"AwayTeam":"Team"},inplace=True)
 
          all_team = pd.concat([home_team,away_team])
          team_stats= all_team.groupby("Team") ["result"].value_counts().unstack(fill_value=0)

          print(team_stats.sort_values(ascending=False,by="W"))
          sort3=team_stats.sort_values(ascending=False,by="W")
          top_t3=sort3.index[0]
          print(f"[bold cyan]{top_t3}  is the Team WIth most W . We can analyse thier result in their position , fisnishing at 1 . [/bold cyan]",emoji.emojize(":Race_Flag:"))
          

          sort3.plot(kind="bar")
          pl.xlabel("Teams")
          pl.ylabel("Result")
          pl.title("Best Team  by Result")
          pl.xticks(rotation=90)
          pl.plot()
          pl.show()
          
        elif n == 4:
          print(emoji.emojize(":trophy:"),"[bold]Best Team by Winrate[/bold]")

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
          top_t4=sort4.index[0]

          print(f"[bold cyan]{top_t4}  is the Team scored most Winrate . We can see as Thier result going. [/bold cyan]",emoji.emojize(":Trophy:"))
          
          sort4.plot(kind="bar")
          pl.title("Best Team By  winning rate")
          pl.xlabel("Team")
          pl.ylabel("WinRate")
          pl.plot()
          pl.show()
         

        elif n == 5  : 
          print(emoji.emojize(":soccer_ball:"),"[bold]Best Team by Goals[/bold]")

          home_g = df[["HomeTeam","FTHG"]].copy() #best away and home team by goals
          home_g= home_g.rename(columns={'FTHG':'Goal',"HomeTeam":"Team"})
          home_g=home_g.groupby('Team') ['Goal'].sum()

          away_g = df[["AwayTeam","FTAG"]].copy()
          away_g = away_g.rename(columns={'FTAG':'Goal',"AwayTeam":"Team"})
          away_g=away_g.groupby('Team') ['Goal'].sum()
         


          all_g=pd.concat([away_g,home_g])
          print(all_g.sort_values(ascending=False))
          sort5=all_g.sort_values(ascending=False)
          top_t5=sort5.index[0]
          print(f"[bold cyan]{top_t5}  is the Team scored most Goals. We can thier result as the champion. This Team is consistent in Home as well as Away matches . [/bold cyan]",emoji.emojize(":Soccer:"))

          sort5.plot(kind="bar")
          pl.title("Best Team By Goals")
          pl.xlabel("Teams")
          pl.ylabel("Goals")
          pl.plot()
          pl.show()
          
        elif n == 6 :
           print(emoji.emojize(":gun:"),"[bold]Best Team by Shotrate[/bold]")

           hs_team = df[["HS","HomeTeam","FTHG"]].copy() #Best team which has shotrate
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
           top_t6=sort6.index[0]
           print(f"[bold cyan]{top_t6}  is the Team wiht most Shotrate . They approach  as fire . Striking opponents defense [/bold cyan]",emoji.emojize(":Fire:"))

           sort6.plot(kind="bar")
           pl.title("Best Team By Shotrate")
           pl.xlabel("Teams")
           pl.ylabel("ShotRate")
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
           top_t7=sort7.index[0]
           print(f"[bold cyan]{top_t7}  is the Team is a Shield . Even if the front of best attack this kept thier arena safe. [/bold cyan]",emoji.emojize(":Shield:"))

           sort7.plot(kind="bar")
           pl.title("Best Defensive Team ")
           pl.xlabel("Team")
           pl.ylabel("DefenseRate")
           pl.plot()
           pl.show()

        elif n == 9 :
           

          teams = sorted(df['HomeTeam'].unique())
          for i ,team in enumerate(teams,1):
             print(f"{i}.{team}")

          chioce= int(input("Enter the team number : "))
          teamnum= teams[chioce-1]
          team_df = df[(df["HomeTeam"]==teamnum) | (df['AwayTeam']==teamnum)]
         
          h_goals = team_df[team_df['HomeTeam']==teamnum] ['FTHG'].sum()
          a_goals = team_df[team_df["AwayTeam"]==teamnum] ['FTAG'].sum()
          t_goals = a_goals + h_goals
          

          wins = len(team_df[
           ((team_df['HomeTeam'] == teamnum) & (team_df['FTR'] == 'H')) |
           ((team_df['AwayTeam'] == teamnum) & (team_df['FTR'] == 'A'))])
          
          matchw= len(team_df)
          winr=wins/matchw

        
          print("Team : ",teamnum)
          print("Total Goals : ",t_goals)
          print("Winrate : ",round(winr,2))



        elif n == 8 :
           win_h=df[['FTR','HomeTeam']].copy()
           win_h.columns=['Result','Team']
           win_h['Points']=win_h['Result'].map({'H':3,'D':1,'A':0})

           win_a=df[['FTR','AwayTeam']].copy()
           win_a.columns=['Result','Team']
           win_a["Points"]=win_a['Result'].map({'H':0,'D':1,'A':3})

           all_win = pd.concat([win_h,win_a])
           all_points= all_win.groupby('Team') ['Points'].sum().sort_values(ascending=False)
           top_t8=all_points.index[0]

           print(f"[bold cyan]{top_t8}  is the Champion Team. We can see thier prgress throughout season making the patter of victory[/bold cyan]",emoji.emojize(":Crown:"))

           for i in track(range(20),description="AND THE CHAMPION IS ......"): time.sleep(0.05) 
           print(f"[bold cyan]{top_t8}  is the Champion Team. We can see thier prgress throughout season making the patter of victory[/bold cyan]",emoji.emojize(":Crown:"))
           print(emoji.emojize(":Soccer:"))
           print("------------------------------------------------------------------")
           print(emoji.emojize(":Crown:"),"SO THE CHAMPION IS ",all_points.head(1))
           print("------------------------------------------------------------------")
          
        
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
   table.add_row("8","Show The Champion Team")

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
          
          
     
    