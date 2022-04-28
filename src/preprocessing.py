import sys
from re import sub

import nltk
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import TweetTokenizer

from logger import Logger

nltk.download('wordnet')
nltk.download('stopwords')

stop = stopwords.words('english')
wnl = WordNetLemmatizer()
stemmer = PorterStemmer()


class Preprocessing:
    """Preprocess a data frame."""

    def __init__(self, df) -> None:
        """Initilize df."""
        try:
            self.df = df
            self.logger = Logger("preprocessing.log").get_app_logger()
            self.logger.info(
                'Successfully Instantiated Preprocessing Class Object')
        except Exception:
            self.logger.exception(
                'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)

    def removePunc(self, myWord):
        """Remove punctuation from string inputs."""
        if myWord is None:
            return myWord
        else:
            return sub('[.:;()/!&-*@$,?^\d+]', '', myWord)

    def removeAscii(self, myWord):
        """Remove ascii from string input."""
        if myWord is None:
            return myWord
        else:
            return str(sub(r'[^\x00-\x7F]+', '', myWord.strip()))

    def lemmatize(self, myWord):
        """Lemmatize words."""
        if myWord is None:
            return myWord
        else:
            return str(wnl.lemmatize(myWord))

    def removeStopWords(self, myWord):
        """Remove stop words."""
        if myWord is None:
            return myWord
        if myWord not in str(stopwords.words('english')):
            return myWord

    def removeLinkUser(self, myWord):
        """Remove web addresses and twitter handles."""
        if not myWord.startswith('@') and not myWord.startswith('http'):
            return myWord

    def prepText(self, myWord):
        """Call other text pre-processing function."""
        try:
            prep = self.removeStopWords(
                self.lemmatize(
                    self.removeAscii(
                        self.removePunc(
                            self.removeLinkUser(
                                myWord.lower()
                            )
                        )
                    )
                )
            )
            self.logger.info(
                'Preprocessed text. Called: removePunc, removeAscii, lemmatize, removeLinkUser methods')
            return prep
        except Exception:
            self.logger.exception(
                'Fails to remove stop words, lemmatize, and clean all tweets')
            sys.exit(1)

    def filterTweetList(self, tweetList):
        """Remove stop words, lemmatize, and clean all tweets."""
        try:
            self.logger.info(
                'Remove stop words, lemmatize, and clean all tweets')
            return [[self.prepText(word) for word
                     in tweet.split()
                     if self.prepText(word) is not None]
                    for tweet in tweetList]
        except Exception:
            self.logger.exception(
                'Fails to filter stop words, lemmatize, and clean all tweets')
            sys.exit(1)

    # def preprocess(self, df):
    #     """Preprocess a data frame."""
    #     df['text'] = df['text'].apply(self.prepText)
    #     return df

    def cleantext(self, org_col, new_col):
        """Clean text.

        Args:
            org_col: Original column to be cleaned
            new_col: New column to hold cleaned text

        Returns:
            df: Dataframe with new column
        """
        try:
            self.df[org_col] = self.df[org_col].astype(str)
            self.df[new_col] = self.df[org_col].str.replace('[^\w\s]', '')
            self.df[new_col] = self.df[new_col].str.replace('\w*\d\w*', '')
            self.df[new_col] = self.df[new_col].apply(
                lambda x: " ".join(x.lower() for x in x.split()))
            self.df[new_col] = self.df[new_col].apply(
                lambda x: " ".join(x for x in x.split() if x not in stop))
            self.logger.info('cleans text')
            return self.df
        except Exception:
            self.logger.exception('Fails to clean text')
            sys.exit(1)

    def stem(self, col):
        """Stemm a word.

        Args:
            col: Column to be stemmed

        Returns:
            df: Dataframe with new column
        """
        try:
            # tokenize each tweet to its root word
            self.df[col] = self.df[col].apply(
                lambda x: " ".join([stemmer.stem(word) for word in x.split()]))
            self.logger.info('tokenizes tweet')
            return self.df
        except Exception:
            self.logger.exception('Fails to tokenize tweet')
            sys.exit(1)
