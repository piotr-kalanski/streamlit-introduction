import streamlit as st
import pandas as pd

st.title('Additional Resources')

st.header('Gallery with examples')
examples = pd.DataFrame(data={
    'title': [
        'Cheat Sheet',
        'Learning Materials',
        'Extras',
        'Snowflake LLM',
        'Gallery'
    ],
    'url': [
        'https://cheat-sheet.streamlit.app/',
        'https://30days.streamlit.app/',
        'https://extras.streamlit.app/',
        'https://arctic.streamlit.app/',
        'https://streamlit.io/gallery'
    ]
})
st.dataframe(
    examples,
    column_config={
        'url': st.column_config.LinkColumn()
    },
    hide_index=True,
)

st.header('Components')
examples = pd.DataFrame(data={
    'title': [
        'Pandas Profiling',
        'Streamlit-Authenticator',
        'Annotated Text Component',
        'Components'
    ],
    'url': [
        'https://github.com/okld/streamlit-pandas-profiling',
        'https://github.com/mkhorasani/Streamlit-Authenticator',
        'https://github.com/tvst/st-annotated-text',
        'https://streamlit.io/components'
    ]
})
st.dataframe(
    examples,
    column_config={
        'url': st.column_config.LinkColumn()
    },
    hide_index=True,
)

st.header('Deployment')
st.write('https://docs.streamlit.io/deploy')
