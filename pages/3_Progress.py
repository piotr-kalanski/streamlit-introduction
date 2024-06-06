import time
import streamlit as st


st.title("Progress and status")
st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(2)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

from utils import display_source_code
display_source_code()
