from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import snscrape.modules.twitter as sntwitter
import pandas as pd
from rest_framework import viewsets
from rest_framework import request
import json
from mysmart.serializers import DataSerializer
# Create your views here.
@api_view(['GET'])
def getScripts(request):
    if request.method == 'GET':
        tweets_list1 = []
        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Immunization in Kenya').get_items()):
            if i>100:
                break
            datajson = {"datetime":tweet.date,"tweetid":tweet.id,"tweet":tweet.rawContent,"username":tweet.user.username}
            tweets_list1.append(datajson)
            
        # # Creating a dataframe from the tweets list above 
        tweets_df1 = pd.DataFrame(tweets_list1)
        serializers = DataSerializer(tweets_df1,many=True)
        b=tweets_df1.to_json()
        return Response(tweets_df1)