
CREATE TABLE TweetInformation
(
    id serial NOT NULL primary key,
    created_at TEXT DEFAULT NULL,
    source VARCHAR(200) DEFAULT NULL,
    original_text TEXT DEFAULT NULL,
    clean_text TEXT DEFAULT NULL,
    sentiment TEXT DEFAULT NULL,
    polarity FLOAT DEFAULT NULL,
    subjectivity FLOAT DEFAULT NULL,
    lang TEXT DEFAULT NULL,
    favourite_count INT DEFAULT NULL,
    retweet_count INT DEFAULT NULL,
    original_author TEXT DEFAULT NULL,
    followers_count INT DEFAULT NULL,
    friends_count INT DEFAULT NULL,
    hashtags VARCHAR(200) DEFAULT NULL,
    user_mentions VARCHAR(200) DEFAULT NULL,
    place TEXT DEFAULT NULL
);

         