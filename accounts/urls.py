from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='login' ),
    path('signup/', views.signup, name='signup' ),
    path('logout/', views.signout, name='logout' ),
    path('profile/', views.profile, name='profile' ),
    path('editprofile/', views.editprofile, name='edit-profile' ),
]
