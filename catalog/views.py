from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """View function for home page of site."""
    return HttpResponse("Welcome from the other side!")
