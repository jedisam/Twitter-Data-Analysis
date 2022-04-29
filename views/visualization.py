import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


def app():
    st.header("Twitter Data Analysis Result")
    st.subheader("Heo")

    image = Image.open('./Images/wordcloud.png')
    st.image(image, caption="Word cloud analysis", use_column_width=True)
