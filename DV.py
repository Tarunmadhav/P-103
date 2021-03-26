import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
figure=px.scatter(df,x="date",y="cases",color="country",title="Covid Cases in various countries")
figure.show()