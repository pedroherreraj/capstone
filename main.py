import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

raw_tweets = pd.read_json(r'./farmers-protest-tweets-2021-03-5.json', lines=True)
raw_tweets = raw_tweets[raw_tweets['lang']=='en']
print("Shape: ", raw_tweets.shape)
raw_tweets.head(5)

# Normalize 'user' field

users = json_normalize(raw_tweets['user'])
users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)
users.head(5)

users = pd.DataFrame(users)
users.drop_duplicates(subset=['userId'], inplace=True)
print("Shape: ", users.shape)
users.head(5)

# Transform 'raw_tweets' DataFrame

# Add column for 'userId'
user_id = []
for user in raw_tweets['user']:
    uid = user['id']
    user_id.append(uid)
raw_tweets['userId'] = user_id

# Remove less important columns
cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
tweets = raw_tweets[cols]
tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)

tweets = pd.DataFrame(tweets)
tweets.drop_duplicates(subset=['tweetId'], inplace=True)
print("Shape: ", tweets.shape)
tweets.head(5)

print("HEADS")
print(tweets.head(5))


def top_ten_retweets(tweets):
    print("Inside")
    print(tweets.head(5))
    top_ten = tweets.sort_values(by=['retweetCount']).head(10)
    return top_ten


a = top_ten_retweets(tweets)
print(a)


