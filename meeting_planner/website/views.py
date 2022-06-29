from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return render(request,"website/welcome.html", {"message": "This is the data sent from the views folder"})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("<h2>This is the about page</h2>")
