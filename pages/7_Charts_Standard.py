import streamlit as st
import numpy as np
import pandas as pd

st.title('Charts - standard')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.header('Bar Chart')
st.bar_chart(chart_data)

st.header('Line Chart')
st.line_chart(chart_data)

st.header('Scatter')
st.scatter_chart(chart_data)

st.header('Area')
st.area_chart(chart_data)

st.header('Map')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

from utils import display_source_code
display_source_code()
