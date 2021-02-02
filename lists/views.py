from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from movies import models as movie_models
from . import models


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"


def toggle_movie(request, movie_pk):
    action = request.GET.get("action", None)

    try:
        movie = movie_models.Movie.objects.get(pk=movie_pk)

        if movie is not None and action is not None:
            the_list, _ = models.List.objects.get_or_create(user=request.user)
            if action == "add":
                the_list.movies.add(movie)
            elif action == "remove":
                the_list.movies.remove(movie)
        return redirect(reverse("movies:movie-detail", kwargs={"pk": movie_pk}))

    except movie_models.Movie.DoesNotExist:
        return redirect(reverse("movies:movie-detail", kwargs={"pk": movie_pk}))
