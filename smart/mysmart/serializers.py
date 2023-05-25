from rest_framework import serializers
from .models import DataM


class DataSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField()
    tweetid = serializers.IntegerField()
    text=serializers.CharField()
    username = serializers.CharField()

    class Meta:  
        model = DataM
        fields = ("datetime","tweetid","text","username") 