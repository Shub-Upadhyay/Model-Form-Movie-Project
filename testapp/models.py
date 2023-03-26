from django.db import models

# Create your models here.
class Movies(models.Model):
    date_in_MM_DD_YY = models.DateField()
    Movie_name = models.CharField(max_length=50)
    Actress_name = models.CharField(max_length=50)
    Actor_name = models.CharField(max_length=50)
    rating = models.FloatField()
