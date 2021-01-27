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

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.star
        if len(all_reviews) == 0:
            return 0

        return round(all_ratings / len(all_reviews), 2)