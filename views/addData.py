import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import exc, inspect
import psycopg2


class DBoperations:

    def DBConnect(self, dbName=None):
        try:
            # engine = create_engine(
            #     'postgresql+psycopg2://postgres:password@localhost/twitter')
            conn = psycopg2.connect(
                user='postgres', password='password', host='127.0.0.1', port='5432'
            )
            cursor = conn.cursor()
            cursor.execute("select version()")
            data = cursor.fetchone()
            print("Connection established to: ", data)
            return conn, cursor
        except exc.SQLAlchemyError as e:
            print("Error", e)
        # conn = mysql.connector.connect(host='localhost', port="3306", user='root', password="",
            #    database=dbName)

    def emojiDB(self, dbName: str) -> None:
        conn, cur = DBoperations.DBConnect(self, 'tweets')
        dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
        cur.execute(dbQuery)
        conn.commit()

    def createDB(self, dbName: str) -> None:
        """
        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :
        Returns
        -------
        """
        conn, cur = DBoperations.DBConnect(self)
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        conn.commit()
        cur.close()

    def createTables(self, dbName: str) -> None:
        """
        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :
        Returns
        -------
        """
        conn, cur = DBoperations.DBConnect(self, 'tweets')
        sqlFile = '/home/bethelhem/Twitter-Data-Analysis/schema.sql'
        fd = open(sqlFile, 'r')
        readSqlFile = fd.read()
        fd.close()

        sqlCommands = readSqlFile.split(';')

        for command in sqlCommands:
            try:
                res = cur.execute(command)
            except Exception as ex:
                print("Command skipped: ", command)
                print(ex)
        conn.commit()
        cur.close()

        return

    def preprocess_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Parameters
        ----------
        df :
            pd.DataFrame:
        df :
            pd.DataFrame:
        df:pd.DataFrame :
        Returns
        -------
        """
        cols_2_drop = ['Unnamed: 0', 'possibly_sensitive']
        try:
            df = df.drop(columns=cols_2_drop, axis=1)
            df = df.fillna(0)
        except KeyError as e:
            print("Error:", e)

        return df

    def insert_to_tweet_table(self, dbName: str, df: pd.DataFrame, table_name: str) -> None:
        """
        Parameters
        ----------
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName:str :
        df:pd.DataFrame :
        table_name:str :
        Returns
        -------
        """
        conn, cur = DBoperations.DBConnect(self, 'tweets')

        df = DBoperations.preprocess_df(self, df)

        for _, row in df.iterrows():
            sqlQuery = f"""INSERT INTO {table_name} (created_at, source, original_text, polarity, subjectivity, lang,
                        favorite_count, retweet_count, original_author, followers_count, friends_count,
                        hashtags, user_mentions, place)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13])

            try:
                # Execute the SQL command
                cur.execute(sqlQuery, data)
                # Commit changes in the database
                conn.commit()
                print("Data Inserted Successfully")
            except Exception as e:
                conn.rollback()
                print("Error: ", e)
        return

    def db_execute_fetch(self, *args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
        """
        Parameters
        ----------
        *args :
        many :
            (Default value = False)
        tablename :
            (Default value = '')
        rdf :
            (Default value = True)
        **kwargs :
        Returns
        -------
        """
        connection, cursor1 = DBoperations.DBConnect(self, 'tweets')
        if many:
            cursor1.executemany(*args)
        else:
            cursor1.execute(*args)

        # get column names
        field_names = [i[0] for i in cursor1.description]

        # get column values
        res = cursor1.fetchall()

        # get row count and show info
        nrow = cursor1.rowcount
        if tablename:
            print(f"{nrow} records from {tablename} table")

        cursor1.close()
        connection.close()

        # return result
        if rdf:
            return pd.DataFrame(res, columns=field_names)
        else:
            return res


st.set_page_config(page_title="Dashboard", layout="wide")


def app():
    try:
        engine = create_engine(
            'postgresql+psycopg2://postgres:password@localhost/twitter')
    except exc.SQLAlchemyError as e:
        print("Error", e)

    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    Y = pd.Series(iris.target, name='class')
    df = pd.concat([X, Y], axis=1)
    df['class'] = df['class'].map(
        {0: "setosa", 1: "versicolor", 2: "virginica"})

    st.write(df)


if __name__ == '__main__':
    db = DBoperations()
    db.createDB("tweets")
    # app()
