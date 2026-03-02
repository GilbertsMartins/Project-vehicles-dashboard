import streamlit as st # type: ignore

intro_page = st.Page(
    "intro_page.py", title="Introdution", icon="📢"
    )

dashboard = st.Page(
    "app.py", title="Dashboard", icon="📊", default=True
    )

pg = st.navigation([intro_page, dashboard])
st.set_page_config(page_title="Used Vehicles Dashboard", page_icon="🚓")
pg.run()