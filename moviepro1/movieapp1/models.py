from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    movieTitle = models.CharField(max_length=39)
    director = models.CharField(max_length=40)
    review_content = models.CharField(max_length=35)
    rating = models.IntegerField()
    created_da = models.DateField()
    review_email_id = models.EmailField()
    status = models.CharField(max_length=39)
    genres = models.CharField(max_length=49)

