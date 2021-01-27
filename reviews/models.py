from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    comment = models.TextField()
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(
        "users.User",
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True, null=True)
    movie = models.ForeignKey(
        "movies.Movie", related_name="reviews", on_delete=models.CASCADE
    )
