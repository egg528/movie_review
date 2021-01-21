from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "rating",
        "runtime",
        "language",
        "genres",
        "poster",
        "imdb_code",
    )
