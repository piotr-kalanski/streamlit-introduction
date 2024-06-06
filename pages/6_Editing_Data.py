import streamlit as st
import pandas as pd

st.title('Editing table')

st.header('Table')
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, disabled=['command'])

st.header('Edition result')
st.table(edited_df)


from utils import display_source_code
display_source_code()
