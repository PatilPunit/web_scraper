
import time

from turtle import st

import pandas as pd
from data_clean import clean_data
import matplotlib.pyplot as pl
from main import df

df = clean_data(df)

win_h=df[['FTR','HomeTeam']].copy()
clean_data(win_h)
win_h.columns=['Result','Team']
win_h['Points']=win_h['Result'].map({'H':3,'D':1,'A':0})

win_a=df[['FTR','AwayTeam']].copy()
win_a.columns=['Result','Team']
win_a["Points"]=win_a['Result'].map({'H':0,'D':1,'A':3})

all_win = pd.concat([win_h,win_a])
all_points= all_win.groupby('Team') ['Points'].sum().sort_values(ascending=False)
top_t8=all_points.index[0]
#   st.write(all_points)
#   st.title("Football analysis")



print("------------------------------------------------------------------")
print("SO THE CHAMPION IS ",all_points.head(1))
print("------------------------------------------------------------------")

