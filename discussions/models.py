from django.db import models
from . import managers


class Discussion(models.Model):

    participants = models.ManyToManyField(
        "users.User", related_name="discussions", blank=True
    )
    movie = models.ForeignKey(
        "movies.Movie", related_name="discussions", blank=True, on_delete=models.CASCADE
    )
    topic = models.CharField(max_length=300)

    objects = managers.CustomModelManager()

    def __str__(self):

        return self.topic + " - " + self.movie.title

    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

    count_messages.short_description = "Number of Messages"


class Message(models.Model):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    discussion = models.ForeignKey(
        "Discussion", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
