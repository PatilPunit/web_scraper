import pandas as pd
import numpy as np 

def select():
   l=[17,18,19,20,21,22,23]
   event = ['E0','E1','E2','E3','EC']
   print("Choose the year for csv file between:")
   for i in l : print(i,i+1)
   year = input("Choose : ")

   print("Choose the event for csv file between:")
   for i in event : print(i)
   event_select= input("Choose : ")
        

    
   link = "https://www.football-data.co.uk/mmz4281/" + year+"/"+event_select+"."+"csv"
   df=pd.read_csv(link)
   print(df)

   run =True
  
   while run == True :
        n = int(input("Enter your choice :"))
        if n == 1:
           print("Show top teams of full time")
           home_goals = df.groupby("HomeTeam") ["FTHG"].max().head()
           away_goals = df.groupby("AwayTeam") ["FTAG"].max().head()
           total_goals = away_goals.add(home_goals,fill_value=0)
           print(total_goals)
    
        elif n==2 :
          print("show top home teams of full time ")
          home_goals = df.groupby("HomeTeam") ["FTHG"].max().head()
          print(home_goals)
          
        elif n==3 :
          print("show top away teams of full time")
          away_goals = df.groupby("AwayTeam") ["FTAG"].max().head()
          print(away_goals)





def main():
    run =True
  
    while run == True :
        n = int(input("Enter your choice :"))
        if n == 1:
           select()

    
        elif n==2 :
          print("show top teams ")
        elif n==3 :
          print("show most goals")
main()
          
     
    