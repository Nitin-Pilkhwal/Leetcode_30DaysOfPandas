import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets[tweets['content'].str.len()>15]
    return mask[['tweet_id']]