import streamlit as st

pg = st.navigation(
    [
        st.Page("home.py", title="Home", icon="📊"),
        st.Page("maps.py", title="Network maps", icon="🗺️"),
    ]
)

pg.run()
