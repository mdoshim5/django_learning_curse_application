from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('create/', views.create),
    path('<int:post_id>/', views.detail),
]