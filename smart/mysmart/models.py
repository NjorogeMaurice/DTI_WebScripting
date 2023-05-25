from django.db import models

# Create your models here.

## Here is the data model
class DataM(models.Model):  
    datetime = models.DateTimeField()  
    tweetid = models.IntegerField()
    tweet=models.CharField(max_length=20000)
    username=models.CharField(max_length=20000)

    def __str__(self):  
        return str(self.tweetid)