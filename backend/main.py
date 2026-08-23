import pandas as pd
from data_clean import clean_data

def select():
    l=[17,18,19,20,21,22,23]
    events = ['E0', 'E1', 'E2', 'E3', 'EC']
    # print("Choose the year for csv file eg.(1718)")
    # for i in l : print(i,i+1)            #loop of years
    # year = input("Choose : ")
    
    # print("Choose the event for csv file between eg.(E1):")
    # for i in events : print(i)             #loop of events
    # event_select= input("Choose : ")

    link = "https://www.football-data.co.uk/mmz4281/" + '1718'+"/"+'E1'+"."+"csv"  #link which acces and bring the data

    global df
    df = pd.read_csv(link)
    print(df.head())

select()



