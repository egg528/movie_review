from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="sign-up"),
    path("login/", views.LogInView.as_view(), name="login"),
    path("login/github/", views.github_login, name="login-github"),
    path("login/github/callback/", views.github_callback, name="github-callback"),
    path("login/kakao/", views.kakao_login, name="login-kakao"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    path("logout/", views.log_out, name="logout"),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.UpdatePasswordView.as_view(), name="password"),
]
