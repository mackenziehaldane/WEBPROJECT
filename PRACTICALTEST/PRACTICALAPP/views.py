from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# from .models import Article


def index(request):
    return HttpResponse("<h1>LATEST NEWS</h1><a href='/rango/about'>Visit our HTML tutorial</a>")


def about(request):
    return HttpResponse("about page")


# def articleView(request):
#     article1 = Article()
#     article1.title = "corona virus"
#     article1.body = "death toll increases"
#     return HttpResponse("articleView page")
