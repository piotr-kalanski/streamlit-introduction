import pandas as pd
import streamlit as st

st.title("Hello World")

st.header("Sample data")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.header("Line chart")
st.line_chart(data=df, x='first column', y='second column')

from utils import display_source_code
display_source_code()
