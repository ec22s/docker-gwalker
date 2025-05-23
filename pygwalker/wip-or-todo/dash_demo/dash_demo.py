import dash
import dash_dangerously_set_inner_html
import pandas as pd
import pygwalker as pyg

df = pd.read_csv("/data/bike_sharing_dc.csv")

app = dash.Dash()

pyg_html_code = pyg.to_html(df, spec="./gw_config.json")

app.layout = dash.html.Div([
  dash_dangerously_set_inner_html.DangerouslySetInnerHTML(pyg_html_code),
])

if __name__ == '__main__':
  app.run_server(debug=True, host='0.0.0.0')
