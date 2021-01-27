from django.contrib import admin
from . import models
from . import forms


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("comment", "star", "user", "movie", "created")