from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Movie
    context_object_name = "movies"
    template_name = "homeview.html"
    paginate_by = 48


class MovieDetailView(DetailView):

    model = models.Movie
    template_name = "movies/movie_detail.html"
