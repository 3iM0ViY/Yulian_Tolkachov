from django.shortcuts import render
from .models import *
from Work.models import *
# Create your views here.

def index(request):
	works = Work.objects.filter(is_published=True)
	context = {
		"works": works,
	}
	return render(request, 'index.html', context)