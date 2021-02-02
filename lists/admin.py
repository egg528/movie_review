from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = ("user", "count_movie")

    search_fields = ("name",)
    filter_horizontal = ("movies",)
