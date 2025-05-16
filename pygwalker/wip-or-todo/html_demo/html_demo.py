import pygwalker as pyg
import pandas as pd


df = pd.read_csv("/data/bike_sharing_dc.csv")

with open("pyg_demo.html", "w", encoding="utf-8") as f:
    html = pyg.to_html(df)
    f.write(html)
