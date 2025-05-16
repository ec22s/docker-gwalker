from typing import List

import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, StreamlitRenderer, PreFilter

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Use Pygwalker In Streamlit")

init_streamlit_comm()

@st.cache_resource
def get_pyg_renderer_bike() -> "StreamlitRenderer":
  df = pd.read_csv("/data/bike_sharing_dc.csv")
  return StreamlitRenderer(df, spec="./gw_config_bike.json")

@st.cache_data
def get_data_billion() -> pd.DataFrame:
  # data source: https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset/data
  return pd.read_csv("/data/Billionaires Statistics Dataset.csv")

@st.cache_data
def get_billion_country() -> List[str]:
  return get_data_billion()["country"].unique().tolist()

@st.cache_resource
def get_pyg_renderer_billion() -> "StreamlitRenderer":
  df = get_data_billion()
  return StreamlitRenderer(df, spec="./gw_config_billion.json")

bike = get_pyg_renderer_bike()
billion = get_pyg_renderer_billion()
pre_filters = []

selected_country = st.multiselect(
  'Billion: select country',
  get_billion_country(),
  []
)
if selected_country:
  pre_filters.append(PreFilter(
    field="country",
    op="one of",
    value=selected_country
  ))
billion.set_global_pre_filters(pre_filters)

tab1, tab2, tab3, tab4 = st.tabs([
  "visual/bike",
  "data",
  "map/billion",
  "charts",
])

with tab1:
  st.subheader("Bike sharing")
  bike.explorer()
with tab2:
  st.subheader("Bike sharing")
  bike.table()
  st.subheader("Billionaires")
  billion.table()
with tab3:
  st.subheader("Billionaires")
  billion.chart(2)
  #  billion.explorer(default_tab="Local Distribution") # NG
with tab4:
  st.subheader("Bike sharing")
  bike.viewer()
  # bike.chart(0)
  bike.chart(1)
  st.subheader("Billionaires")
  billion.chart(1)
  billion.chart(3)
  billion.chart(4)
