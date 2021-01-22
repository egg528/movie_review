from django.shortcuts import render, reverse, redirect
from django.views.generic import DetailView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models, forms


class SignUpView(FormView):

    form_class = forms.SignUpForm
    template_name = "users/signup.html"

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogInView(FormView):

    template_name = "users/login.html"
    form_class = forms.LogInForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(user)
        if user is not None:
            login(self.request, user)
            messages.success(request, f"Welcome back {user.last_name}")
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    messages.info(request, "See you later")
    logout(request)
    return redirect(reverse("core:home"))