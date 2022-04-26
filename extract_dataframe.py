import json
import pandas as pd

from textblob import TextBlob


def read_json(json_file: str) -> list:
    """Json file reader to open and read json files into a list.

    Args:
    -----
    json_file: str - path of a json file
    Returns
    -------
    length of the json file and a list of json
    """
    tweets_data = []
    for tweets in open(json_file, 'r'):
        tweets_data.append(json.loads(tweets))
    return len(tweets_data), tweets_data


class TweetDfExtractor:
    """Return  function will parse tweets json into a pandas dataframe.

    Return
    ------
    dataframe
    """

    def __init__(self, tweets_list):
        """Initialize the class TweetDfExtractor.

        Args:
            tweet_list(List): Initializes the class with list.
        """
        self.tweets_list = tweets_list

    def find_statuses_count(self) -> list:
        """_summary_statuses_count.

        Returns:
            list: Returns a list of statuses count
        """
        statuses_count = [data['user']['statuses_count']
                          if 'user' in data else '' for data in self.tweets_list]
        return statuses_count

    def find_full_text(self) -> list:
        """_summary_statuses_count.

        Returns:
            list: Returns a list of full_text
        """
        text = [data['text'] for data in self.tweets_list]
        return text

    def find_sentiments(self, text) -> list:
        """Find sentiment of a given text.

        Args:
            text (str): A text to be analyzed.

        Returns:
            list: a list of analyzed text.
        """
        polarity, subjectivity = [], []
        for tweet in text:
            blob = TextBlob(tweet)
            sentiment = blob.sentiment
            polarity.append(sentiment.polarity)
            subjectivity.append(sentiment.subjectivity)

        return polarity, subjectivity

    def find_created_time(self) -> list:
        """Find created_at time of a tweet.

        Returns:
            list: A list of created_at time.
        """
        created_at = [data['created_at'] for data in self.tweets_list]
        return created_at

    def find_source(self) -> list:
        """Find the source of each tweet.

        Returns:
            list: A list of source.
        """
        source = [data['source'] for data in self.tweets_list]

        return source

    def find_screen_name(self) -> list:
        """Find screen_name.

        Returns:
            list: A list of screen name.
        """
        screen_name = [data['user']['screen_name']
                       if 'user' in data else '' for data in self.tweets_list]
        return screen_name

    def find_followers_count(self) -> list:
        """Find followers count.

        Returns:
            list: A list of followers count.
        """
        followers_count = [data['user']['followers_count']
                           if 'user' in data else 0 for data in self.tweets_list]
        return followers_count

    def find_friends_count(self) -> list:
        """Find friends count.

        Returns:
            list: A list of friends count.
        """
        friends_count = [data['user']['friends_count']
                         if 'user' in data else 0 for data in self.tweets_list]
        return friends_count

    def is_sensitive(self) -> list:
        """Check sensitivity of tweets.

        Returns:
            list: _description_
        """
        is_sensitive = [data['possibly_sensitive']
                        if 'possibly_sensitive' in data.keys() else '' for data in self.tweets_list]

        return is_sensitive

    def find_favourite_count(self) -> list:
        """Find favourite count of each tweet.

        Returns:
            list: A list of favourite count.
        """
        favorite_count = [data['retweeted_status']['favorite_count']
                          if 'retweeted_status' in data.keys() else 0 for data in self.tweets_list]

        return favorite_count

    def find_retweet_count(self) -> list:
        """Find retweet count of each tweet.

        Returns:
            list: A list of retweet count.
        """
        retweet_count = [data['retweeted_status']['retweet_count']
                         if 'retweeted_status' in data.keys() else 0 for data in self.tweets_list]
        return retweet_count

    def find_hashtags(self) -> list:
        """Find hashtags of each tweet.

        Returns:
            list: A list of hastags.
        """
        hashtags = [data['entities']['hashtags'] if 'entities' in data.keys(
        ) else '' for data in self.tweets_list]
        return hashtags

    def find_mentions(self) -> list:
        """Find mentions of each tweet.

        Returns:
            list: A list of mentions.
        """
        mentions = [data['entities']['user_mentions']
                    if 'entities' in data.keys(
        ) else '' for data in self.tweets_list]
        return mentions

    def find_lang(self) -> list:
        """Find lang of tweets.

        Returns:
            list: A list of all lang
        """
        lang = [data['lang'] for data in self.tweets_list]

        return lang

    def find_location(self) -> list:
        """Find location of each tweet.

        Returns:
            list: A list of location.
        """
        location = [data['user']['location']
                    if 'user' in data.keys(
        ) else '' for data in self.tweets_list]

        return location

    def get_tweet_df(self, save=True) -> pd.DataFrame:
        """Save a processed tweet list."""
        columns = ['created_at', 'source', 'original_text', 'polarity',
                   'subjectivity', 'lang', 'favourite_count', 'retweet_count',
                   'original_author', 'followers_count', 'friends_count',
                   'possibly_sensitive', 'hashtags', 'user_mentions', 'place']

        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        # print("LOCC: ", location[:100])
        data = zip(created_at, source, text, polarity, subjectivity,
                   lang, fav_count, retweet_count, screen_name, follower_count,
                   friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')

        return df


if __name__ == "__main__":
    # required column to be generated you should be creative
    columns = ['created_at', 'source', 'original_text', 'clean_text',
               'sentiment', 'polarity', 'subjectivity', 'lang',
               'favorite_count', 'retweet_count', 'original_author',
               'screen_count', 'followers_count', 'friends_count',
               'possibly_sensitive', 'hashtags', 'user_mentions',
               'place', 'place_coord_boundaries']
    _, tweet_list = read_json("./data/Economic_Twitter_Data.json")

    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df()

    # use all defined functions to generate a dataframe
