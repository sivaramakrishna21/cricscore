from django.urls import path, re_path as url
from onlineapp.views.colleges import CollegeView, addcollege,loginfor,signfor,logout_user,addstudents
from onlineapp.views import colleges
from . import views


app_name = "onlineapp"

urlpatterns = [
    path("colleges/<str:acronym>/add",addstudents.as_view(),name="add student"),
    path("logout/",logout_user.as_view(),name="logout"),
    path("login/",loginfor.as_view(),name="login"),
    path("signup/",signfor.as_view(),name="signup"),
    path("colleges/edit/<int:pk>/", addcollege.as_view(), name="edit list"),
    path("colleges/delete/<int:pk>",addcollege.as_view(),name="delete college"),
    path("colleges/", CollegeView.as_view(), name="College_list"),
    path("colleges/add", addcollege.as_view(), name="form"),
    path("colleges/<str:acronym>", CollegeView.as_view(), name="studemt list"),

]
