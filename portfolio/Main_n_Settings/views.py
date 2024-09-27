from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	context = {

	}
	return render(request, 'index.html', context)

def work(request):
	context = {

	}
	return render(request, 'work.html', context)

def blog(request):
	context = {

	}
	return render(request, 'blog.html', context)