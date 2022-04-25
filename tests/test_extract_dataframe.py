import os
import sys
import unittest

import pandas as pd
from extract_dataframe import TweetDfExtractor, read_json

sys.path.append(os.path.abspath(os.path.join('../..')))


_, tweet_list = read_json("data/Economic_Twitter_Data.json")

columns = ['created_at', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang', 'favorite_count', 'retweet_count',
           'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']


class TestTweetDfExtractor(unittest.TestCase):
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
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    # def test_find_statuses_count(self):
    #     """Test find status count module."""
    #     self.assertEqual(self.df.find_statuses_count(), [
    #                      204051, 3462, 6727, 45477, 277957])

    def test_find_full_text(self):
        """Test find full text method."""
        text = ['RT @nikitheblogger: Irre: Annalena Baerbock sagt, es bricht ihr das Herz, dass man nicht bedingungslos schwere Waffen liefert.', 'Mir bricht e…', 'RT @sagt_mit: Merkel schaffte es in 1 Jahr 1 Million "Flüchtlinge" durchzufüttern, jedoch nicht nach 16 Jahren 1 Million Rentner aus der Ar…', 'RT @Kryptonoun: @WRi007 Pharma in Lebensmitteln, Trinkwasser, in der Luft oder in der Zahnpasta irgendwo muss ein Beruhigungsmittel bzw. Be…', ''



                "Thank you @research2note for creating this amazing campaign &amp; turning social media #red4research today. @NHSRDFORUM is all about sharing the talent, passion  &amp; commitment of individuals coming together as a community for the benefit of all. You've done this. Well done 👋", 'Former Pfizer VP and Virologist, Dr. Michael Yeadon, is one of the most credentialed medical professionals speaking out about the dangers of the #Covid19 vaccines, breaks down his “list of lies” that keeps him up at night. https://t.co/LSE8CrKdqn', 'I think it’s important that we don’t sell COVAX short. It still has a lot going for it and is innovative in its design. But it needs more vaccines to share.  We’re hoping our low cost @TexasChildrens recombinant protein COVID19 vaccine with @biological_e will help fill some gaps']

        self.assertEqual(self.df.find_full_text(), text)

    def test_find_sentiments(self):
        """Test find sentiment module."""
        self.assertEqual(self.df.find_sentiments(self.df.find_full_text()), ([0.16666666666666666, 0.13333333333333333, 0.3166666666666667, 0.08611111111111111, 0.27999999999999997], [
                         0.18888888888888888, 0.45555555555555555, 0.48333333333333334, 0.19722222222222224, 0.6199999999999999]))

    def test_find_created_time(self):
        """Test find created time module."""
        created_at = ['Fri Jun 18 17:55:49 +0000 2021', 'Fri Jun 18 17:55:59 +0000 2021', 'Fri Jun 18 17:56:07 +0000 2021',
                      'Fri Jun 18 17:56:10 +0000 2021', 'Fri Jun 18 17:56:20 +0000 2021']

        self.assertEqual(self.df.find_created_time(), created_at)

    def test_find_source(self):
        """Test find source module."""
        source = ['<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                  '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                  '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>']

        self.assertEqual(self.df.find_source(), source)

    def test_find_screen_name(self):
        """Test find screen name module."""
        name = ['ketuesriche', 'Grid1949',
                'LeeTomlinson8', 'RIPNY08', 'pash22']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        """Test find follower count module."""
        f_count = [551, 66, 1195, 2666, 28250]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        """Test find friend count module."""
        friends_count = [351, 92, 1176, 2704, 30819]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        """Test find is sensetive module."""
        self.assertEqual(self.df.is_sensitive(), [
                         None, None, None, None, None])

    def test_find_favourite_count(self):
        """Test find favourite count module."""
        self.assertEqual(self.df.find_favourite_count(),
                         [548, 195, 2, 1580, 72])

    def test_find_retweet_count(self):
        """Test find retweet count module."""
        self.assertEqual(self.df.find_retweet_count(), [612, 92, 1, 899, 20])

    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )

    def test_find_location(self):
        """Test find location module."""
        self.assertEqual(self.df.find_location(), [
                         'Mass', 'Edinburgh, Scotland', None, None, 'United Kingdom'])


if __name__ == '__main__':
    unittest.main()
