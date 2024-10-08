"""URL mappings for the user API"""

from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("register/", views.CreateUserVIew.as_view(), name="register"),
    path("login/", views.CreateTokenView.as_view(), name="login"),
    path("me/", views.ManageUserVIew.as_view(), name="me"),
]
