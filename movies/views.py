from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, FormView
from django.contrib import messages
from django.db.models import Q
from . import models, forms
from reviews import forms as review_forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Movie
    context_object_name = "movies"
    template_name = "homeview.html"
    paginate_by = 48


class MovieDetailView(DetailView):

    model = models.Movie
    template_name = "movies/movie_detail.html"

    form_class = review_forms.CreateReviewForm

    def get_success_url(self):
        return redirect(
            reverse("movies:detail", kwargs={"pk": self.kwargs.get("movie_id")})
        )

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context["form"] = review_forms.CreateReviewForm(initial={"movie": self.object})
        context["reviews"] = self.object.reviews.filter(
            movie_id=self.kwargs.get("movie_id")
        )
        return context


def SearchView(request):
    br = models.Movie.objects.all()

    b = request.GET.get("moviename", "")
    if b:
        br = br.filter(title__icontains=b)

    return render(
        request, "movies/movie_search.html", {"movie_search": br, "movie_name": b}
    )
