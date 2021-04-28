from django.urls import path

from .views import HomePageView, AboutPageView, CvPageView, AccountPageView, insertUser

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("cv/", CvPageView.as_view(), name="cv"),
    path("account/", insertUser, name="account"),
]
