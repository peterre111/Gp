from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home' , views.home, name="home"),
    path('features', views.features, name="features"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]