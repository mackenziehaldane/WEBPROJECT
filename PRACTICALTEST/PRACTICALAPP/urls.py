from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home-page"),
    path('rango/about', views.about, name="about-page"),
]

