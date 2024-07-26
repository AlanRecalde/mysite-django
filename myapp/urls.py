from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.about),
    path('projects/', views.projects),
    path('task/<str:tittle>', views.tasks),
]