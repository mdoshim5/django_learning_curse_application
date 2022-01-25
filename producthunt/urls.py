from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='producthunt'),
    path('<int:product_id>/', views.product_details),
    path('create', views.create),
]