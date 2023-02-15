from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    mycontext = {
        "name": "Your name",
        "class": "Senior"
    }
    return render(request, "index.html", context=mycontext)

def login_view(request):
    return render(request, "login.html")