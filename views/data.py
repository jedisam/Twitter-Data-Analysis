import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets


def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `Econmoic` dataset.")
    # st.text_input("Enter the number of rows", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    df = pd.read_csv('./clean_tweet.csv', nrows=number)

    # iris = datasets.load_iris()
    # X = pd.DataFrame(iris.data, columns=iris.feature_names)
    # Y = pd.Series(iris.target, name='class')
    # df = pd.concat([X, Y], axis=1)
    # df['class'] = df['class'].map(
    #     {0: "setosa", 1: "versicolor", 2: "virginica"})

    st.write(df)
