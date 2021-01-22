from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),
]
