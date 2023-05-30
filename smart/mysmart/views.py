from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import snscrape.modules.twitter as sntwitter
import pandas as pd
from .sentiment import *
# Create your views here.
# Create your views here.
@api_view(['GET'])
def getScripts(request):
    # paginator.page_size = 10
    if request.method == 'GET':
        tweets_list1 = []
        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Immunization in Kenya').get_items()):
            if i>100:
                break
            datajson = {"datetime":tweet.date,"tweetid":tweet.id,"tweet":tweet.rawContent,"username":tweet.user.username,"likes_count":tweet.likeCount}
            tweets_list1.append(datajson)

        # # Creating a dataframe from the tweets list above
        tweets_df1 = pd.DataFrame(tweets_list1)
        clean=[]
        for tweet in tweets_df1['tweet']:
            clean.append(clean_tweet(tweet))
        tweets_df1['clean'] = clean
        clean_Se = get_sentiment(tweets_df1)
        clean_list = []
        for row in clean_Se:
            datajson = {"datetime":row[0],"tweetid":row[1],"tweet":row[2],"like_count":row[4],"cleandata":row[5],"sentiment":row[8],"username":row[3],"polarity":row[7],"subjectivity":row[6],"neg":row[9],"neu":row[10],"pos":row[11],"compound":row[12]}
            clean_list.append(datajson)

        # serializers = DataSerializer(tweets_df1,many=True)
        # b=tweets_df1.to_json()
        # return Response(pd.Series(clean_list))
        return Response(pd.Series(clean_list))

@api_view(['GET'])
def getOne(request,query):
    if request.method == 'GET':
        tweets_list1 = []
        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i>100:
                break
            datajson = {"datetime":tweet.date,"tweetid":tweet.id,"tweet":tweet.rawContent,"username":tweet.user.username,"likes_count":tweet.likeCount}
            tweets_list1.append(datajson)

        # # Creating a dataframe from the tweets list above
        tweets_df1 = pd.DataFrame(tweets_list1)
        clean=[]
        for tweet in tweets_df1['tweet']:
            clean.append(clean_tweet(tweet))
        tweets_df1['clean'] = clean
        clean_Se = get_sentiment(tweets_df1)
        clean_list = []
        for row in clean_Se:
            datajson = {"datetime":row[0],"tweetid":row[1],"tweet":row[2],"like_count":row[4],"cleandata":row[5],"sentiment":row[8],"username":row[3],"polarity":row[7],"subjectivity":row[6],"neg":row[9],"neu":row[10],"pos":row[11],"compound":row[12]}
            clean_list.append(datajson)
        return Response(pd.Series(clean_list))
