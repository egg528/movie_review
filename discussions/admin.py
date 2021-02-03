from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Discussion)
class DiscussionAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )

    filter_horizontal = ("participants",)