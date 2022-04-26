import os
import sys
import unittest

import pandas as pd
import numpy
from pandas._libs.tslibs.timestamps import Timestamp

from clean_tweets_dataframe import Clean_Tweets

sys.path.append(os.path.abspath(os.path.join('../..')))


class TestTweetDfClean(unittest.TestCase):
    """A class for unit-testing function in the fix_clean_tweets_dataframe.py file.

    Args:
        unittest.TestCase this allows the new class to inherit
        from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        """Dataframe that contains the data from the covid19.json file.

        Returns:
            pd.DataFrame: DF from Economic_Twitter_data.json file.
        """
        self.df = self.df = pd.DataFrame({'created_at': [
                                         '4/4/2021 12:01'], 'polarity': ['0.0'], 'retweet_count': ['0.0'], 'favourite_count': ['1.0'], 'lang': 'de', 'original_text': 'test text 1'}, {'created_at': [
                                             '6/2/2022 10:25'], 'polarity': ['1.0'], 'retweet_count': [3.0], 'favourite_count': [3.0], 'lang': 'de', 'original_text': 'test text 1'})
        # tweet_df = self.df.get_tweet_df()

    def test_convert_to_datetime(self):
        """Test convert to datetime module."""
        df = Clean_Tweets(self.df).convert_to_datetime(self.df)
        assert type(df['created_at'][0]) is Timestamp

    def test_convert_to_numbers(self):
        """Test convert to number module."""
        df = Clean_Tweets(self.df).convert_to_numbers(self.df)
        assert type(df['polarity'][0]) is numpy.float64 and type(
            df['retweet_count'][0]) is numpy.float64 and type(df['favourite_count'][0]) is numpy.float64

    def test_remove_non_english_tweets(self):
        """Test remove non english tweets module."""
        df = Clean_Tweets(self.df).remove_non_english_tweets(self.df)
        assert df.shape[0] == 0

    def test_drop_duplicate(self):
        """Test convert to datetime module."""
        df = Clean_Tweets(self.df).drop_duplicate(self.df)
        assert df.shape[0] == 1


if __name__ == '__main__':
    unittest.main()
