from django.urls import path

from educations import views

app_name = 'educations'

urlpatterns = [
  path('', views.education_list, name='education_list'),
  path('new/', views.education_create, name='education_new'),
  path('edit/<int:pk>/', views.education_update, name='education_edit'),
  path('delete/<int:pk>/', views.education_delete, name='education_delete'),
]