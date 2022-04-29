from PIL import Image
import sys
import os
import streamlit as st

# sys.path.append(os.path.abspath(os.path.join('../')))


def app():
    st.title('Home')

    st.write("Trending topics about world's Economics.")

    st.write(
        'Go to the data navigation to learn more about the data and the visualization page to get insight of the Data.')
    # col1, col2 = st.columns(2)
    image = Image.open('../Images/wordcloud.png')
    st.image(image, caption="Word cloud analysis", use_column_width=True)

    # # image = Image.open('./wordcloud.png')
    # st.image(image, caption='Enter any caption here')

    # col1.image(image, caption='World Economic Trends', use_column_width=True)
