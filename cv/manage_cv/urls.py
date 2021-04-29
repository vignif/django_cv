from django.urls import path

from manage_cv import views

app_name = 'manage_cv'

urlpatterns = [
  path('', views.home, name='home'),
]