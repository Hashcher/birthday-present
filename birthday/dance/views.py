from django.shortcuts import render

# Create your views here.


def trust(request):
    return render(request, "home.html")


def message(request):
    return render(request, "message.html")
