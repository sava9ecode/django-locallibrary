from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """View function for home page of site."""
    return HttpResponse("This is my first Local Library app. It works!")
