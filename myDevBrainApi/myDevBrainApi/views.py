from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Welcome to My Dev Brain, an app to act as my brain for managing dev projects! Better than a spreadsheet!")
