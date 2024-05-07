from django.shortcuts import render

from .models import Member

# Create your views here.


def index(request):
    mem = Member.objects.all()
    return render(request, "index.html", {"mem": mem})

def about(request):
    mem = Member.objects.all()
    return render(request, "about.html", {"mem": mem})
