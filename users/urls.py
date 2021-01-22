from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="sign-up"),
    path("login", views.LogInView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
]
