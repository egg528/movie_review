from django.urls import path
from movies import views as movie_views

app_name = "core"

urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="home"),
]
