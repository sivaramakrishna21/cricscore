from django.urls import path, re_path as url,include
from cricscore.views.displaymatches import matchView,logout_user,loginfor,signfor,displaypoints,displayteamdetails
from . import views

app_name = "cricscore"

urlpatterns = [
    path("home/<str:team>",displayteamdetails.as_view(),name="details"),
    path("home/",matchView.as_view(),name="home"),
    path("home/<int:season>/<int:id1>",matchView.as_view(),name="seasons"),
    path("home/<int:season>/summary/<int:id>/",matchView.as_view(),name="matc"),
    path("logout/", logout_user.as_view(), name="logout"),
    path("login/", loginfor.as_view(), name="login"),
    path("signup/", signfor.as_view(), name="signup"),
    path("home/<int:season>/points",displaypoints.as_view(),name="points"),


]
