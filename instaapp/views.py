from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile


# Create your views here.

# @login_required(login_url='accounts/login/')

def welcome(request):
    posts=Image.objects.all()
    return render(request, 'index.html', {"images":posts})
