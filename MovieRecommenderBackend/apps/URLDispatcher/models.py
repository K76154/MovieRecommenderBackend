from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=11)
    link = models.URLField()
    average_rating = models.FloatField()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-average_rating']


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['user_id']


class RatingData(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(null=False, blank=False)
    timestamp = models.BigIntegerField(null=True, blank=False)

    class Meta:
        verbose_name = 'Rating Data'
        verbose_name_plural = 'Rating Data'

