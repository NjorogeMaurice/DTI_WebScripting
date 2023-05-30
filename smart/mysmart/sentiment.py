from textblob import TextBlob
import nltk
import re
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        # tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        tweet=tweet.lower()
        ## remove mentions and hashtags
        tweet = re.sub(r"@(\w+)","",tweet)
        tweet = re.sub(r"#(\w+)","",tweet)
        tweet = re.sub(r"&(\w+);","",tweet)

        ## remove urls
        tweet = re.sub(r"http\S+","",tweet)
        ## remove other unspecified special characters
        tweet = re.sub(r"…","",tweet)
        tweet = re.sub(r"’s","",tweet)
        tweet = re.sub(r"\n"," ",tweet)
        ## removing punctuation
        tweet = tweet.translate(str.maketrans('','',string.punctuation))
        ## removing digits
        tweet = tweet.translate(str.maketrans('','',string.digits))

        return remove_emojis(tweet)


def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def get_sentiment(tweet_data):
    #Calculating Negative, Positive, Neutral and Compound values
    tweet_data[['polarity', 'subjectivity']] = tweet_data['clean'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
    for index, row in tweet_data['clean'].items():
     score = SentimentIntensityAnalyzer().polarity_scores(row)
     neg = score['neg']
     neu = score['neu']
     pos = score['pos']
     comp = score['compound']
     if neg > pos:
      tweet_data.loc[index, 'sentiment'] = "negative"
     elif pos > neg:
      tweet_data.loc[index, 'sentiment'] = "positive"
     else:
      tweet_data.loc[index, 'sentiment'] = "neutral"
     tweet_data.loc[index, 'neg'] = neg
     tweet_data.loc[index, 'neu'] = neu
     tweet_data.loc[index, 'pos'] = pos
     tweet_data.loc[index, 'compound'] = comp
    return tweet_data.values.tolist()