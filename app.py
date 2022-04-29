import streamlit as st
from multiapp import MultiApp
from views import home, data, visualization

st.set_page_config(page_title="Economic Data Analysis")

app = MultiApp()


st.title("Tweet Sentiment Analysis")

st.markdown("""
            # Economic Data Analysis
            Twitter Data Analysis of Economic Data
            """)

app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Visualization", visualization.app)

#  main app
app.run()
