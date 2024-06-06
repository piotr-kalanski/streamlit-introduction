import streamlit as st

st.title("Basic Inputs")

vars = {}

st.header('Form')
vars['checkbox'] = st.checkbox('yes')
vars['button'] = st.button('Click')
vars['radio'] = st.radio('Pick your gender', ['Male', 'Female'])
vars['selectbox'] = st.selectbox('Pick your gender', ['Male', 'Female'])
vars['multiselect'] = st.multiselect('choose a planet', ['Jupiter', 'Mars', 'neptune'])
vars['select_slider'] = st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
vars['slider'] = st.slider('Pick a number', 0.50)

st.header('Your selections')
st.json(vars)

st.header('More inputs')
st.write('https://docs.streamlit.io/develop/api-reference/widgets')

from utils import display_source_code
display_source_code()
