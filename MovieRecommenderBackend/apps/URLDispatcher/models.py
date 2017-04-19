from django.db import models


class Movie(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=255)
    rating = models.FloatField(blank=False)
    link = models.URLField()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-rating']

