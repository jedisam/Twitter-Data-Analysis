from views import addData
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from decouple import config


def app():
    host = config('Host', default='')
    database = config('Database', default='')
    user = config('User', default='')
    password = config('Password', default='')
    port = config('Port', default='')
    db1 = addData.DBoperations(host, database, user, password, port)
    conn = db1.createDB()

    st.sidebar.markdown(
        "Twitter Data Filter")

    all_tweets = pd.read_sql_query('select * from tweetinformation', conn)
    conn.close()
    print(all_tweets.shape)
    print(all_tweets.head())

    if st.checkbox("Show Data"):
        st.write(all_tweets.head(40))

    name_search = st.text_input("Search tweets by author name")
    if st.button("search"):
        # 1. only name/nickname is checked
        # if name is specified
        if name_search != '':
            df_result_search = all_tweets[all_tweets['original_author'].str.contains(
                name_search, case=False, na=False)]
        # if user does not enter anything
        else:
            st.warning('Please enter at least a name or a nickname')

        st.write("{} Records ".format(str(df_result_search.shape[0])))
        st.dataframe(df_result_search)

    tweet = st.radio("sentiment Type", ("positive", "negative", "neutral"))
    # st.write(all_tweets.query("sentiment == @tweet")
    #          [['text']].sample(1).iat[0, 0])

    select = st.sidebar.selectbox('Visualisation Of Tweets', [
                                  'Histogram', 'Pie Chart'], key=1)

    sentiment = all_tweets['sentiment'].value_counts()

    sentiment = pd.DataFrame(
        {'Sentiment': sentiment.index, 'Tweets': sentiment.values})
    st.markdown("###  Sentiment count")
    if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='Tweets',
                     color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

    # slider
    st.sidebar.markdown('Time & Location of tweets')
    hr = st.sidebar.slider("Hour of the day", 0, 23)
    all_tweets['Date'] = pd.to_datetime(
        all_tweets['created_at'], format='%Y-%m-%d %H:%M:%S')
    # hr_data = all_tweets[all_tweets['created_at'].dt.hour == hr]
    # if not st.sidebar.checkbox("Hide", True, key='1'):
    #     st.markdown("### Location of the tweets based on the hour of the day")
    #     st.markdown("%i tweets during  %i:00 and %i:00" %
    #                 (len(hr_data), hr, (hr+1) % 24))
    #     st.map(hr_data)

    image = Image.open('../Images/wordcloud.png')
    st.image(image, caption="Word cloud analysis", use_column_width=True)
