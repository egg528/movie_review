from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
    path("toggle/<int:movie_pk>", views.toggle_movie, name="toggle-movie"),
]
