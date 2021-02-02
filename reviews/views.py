from django.contrib import messages
from django.shortcuts import redirect, reverse, get_object_or_404
from movies import models as movie_models
from . import forms, models

# Create your views here.


def create_review(request, movie):

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        movie = movie_models.Movie.objects.get(id=movie)
        if not movie:
            return redirect(reverse("movies:movie-detail", kwargs={"pk": movie.id}))
        if form.is_valid():
            review = form.save()
            review.movie = movie
            review.user = request.user
            review.save()
            form.save_m2m()
            messages.success(request, "Create Comment")
            return redirect(reverse("movies:movie-detail", kwargs={"pk": movie.id}))