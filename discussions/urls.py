from django.urls import path
from . import views

app_name = "discussions"

urlpatterns = [
    path("go/<int:dis_pk>/", views.go_discussion, name="go"),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
    path("create/<int:movie>/", views.CreateDiscussionView.as_view(), name="create"),
]
