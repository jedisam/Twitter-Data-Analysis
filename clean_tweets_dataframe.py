import pandas as pd


class Clean_Tweets:
    """The PEP8 Standard AMAZING!!!."""

    def __init__(self, df: pd.DataFrame):
        """Initialize the class dataframe.

        Args:
            df(pd.DataFrame): Initializes the class dataframe.
        """
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove rows that has column names.

        This error originated from the data collection stage.
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count'].index
        self.df = df.drop(unwanted_rows, inplace=True)
        self.df = df[df['polarity'] != 'polarity']

        # self.drop_duplicate(self.df)
        return self.df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """Drop duplicate rows."""
        self.df = df.drop_duplicates(subset='original_text')

        # self.convert_to_datetime(self.df)
        return self.df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert column to datetime."""
        self.df['created_at'] = pd.to_datetime(
            df['created_at'], errors='coerce')

        self.df = df[df['created_at'] >= '2020-12-31']

        # self.convert_to_numbers(self.df)
        return self.df

    def convert_to_numbers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert columns like polarity, subjectivity, favorite_count, retweet_count to numbers."""
        self.df['polarity'] = pd.to_numeric(
            df['polarity'], errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(
            df['retweet_count'], errors='coerce')
        self.df['favourite_count'] = pd.to_numeric(
            df['favourite_count'], errors='coerce')

        # self.remove_non_english_tweets(self.df)
        return self.df

    def remove_non_english_tweets(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove non english tweets from language column."""
        self.df = df.query("lang == 'en' ")

        # self.df.to_csv('processed_tweet_data.csv', index=False)
        # print('File Successfully Saved.!!!')
        return self.df


if __name__ == "__main__":
    tweet_df = pd.read_csv("./processed_tweet_data.csv")
    cleaner = Clean_Tweets(tweet_df)
    # print(cleaner.df.head())
    df = cleaner.drop_unwanted_column(cleaner.df)
    df = cleaner.drop_duplicate(df)
    df = cleaner.convert_to_numbers(df)
    df = cleaner.convert_to_datetime(df)
    df = cleaner.remove_non_english_tweets(df)

    df.to_csv('cleaned_tweet_data.csv', index=False)
