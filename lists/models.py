from django.db import models


class List(models.Model):

    user = models.OneToOneField(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    movies = models.ManyToManyField("movies.Movie", blank=True)

    def __str__(self):
        return str(self.user)

    def count_movie(self):
        return self.movies.count()
