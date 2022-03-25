import pandas as pd
import plotly.graph_objects as jo

df = pd.read_csv('C107/data.csv')
studf = df.loc[df['student_id'] == 'TRL_abc' ]
data = studf.groupby("level")["attempt"].mean() 
gr = jo.Figure(jo.Bar(x = data , y = ['Level 1','Level 2','Level 3','Level 4'] , orientation = 'h'))
gr.show()