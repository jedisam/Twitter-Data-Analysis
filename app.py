import streamlit as st
from multiapp import MultiApp
from views import home, data, visualization

app = MultiApp()

st.set_page_config(page_title="Economic Data Analysis")

st.title("Tweet Sentiment Analysis")

st.markdown("""
            # Economic Data Analysis
            Twitter Data Analysis of Economic Data
            """)

app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", visualization.app)

#  main app
app.run()
