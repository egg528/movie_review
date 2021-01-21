from django.db import models


class Movie(models.Model):

    imdb_code = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=300)
    year = models.IntegerField()
    rating = models.FloatField()
    runtime = models.IntegerField()
    summary = models.TextField()
    language = models.CharField(max_length=10)
    genres = models.CharField(max_length=100)
    poster = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-year",)
