from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is the Index Page")

def help_view(request):
    help_dict = {"help_text": "This is the help text which is currently a string..."}
    return render(request, "app_five/help.html", context=help_dict)
