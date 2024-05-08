from django.shortcuts import render

from .models import About, Member
from django.shortcuts import render, redirect
from .models import Contact


def index(request):
    mem = Member.objects.all()
    return render(request, "index.html", {"mem": mem})


def about(request):
    abt = About.objects.all()
    return render(request, "about.html", {"abt": abt})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, "contact.html")
