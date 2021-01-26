from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.contrib import messages
from django.db.models import Q
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Movie
    context_object_name = "movies"
    template_name = "homeview.html"
    paginate_by = 48


class MovieDetailView(DetailView):

    model = models.Movie
    template_name = "movies/movie_detail.html"


def SearchView(request):
    br = models.Movie.objects.all()

    b = request.GET.get("moviename", "")
    if b:
        br = br.filter(title__icontains=b)

    return render(
        request, "movies/movie_search.html", {"movie_search": br, "movie_name": b}
    )
