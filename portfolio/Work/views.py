from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.

def index(request):
	context = {

	}
	return render(request, 'work.html', context)

def work_detail(request, work):
	work = get_object_or_404(Work, is_published = True, slug = work,)
	carousel = CarouselItem.objects.filter(work=work)
	context = {
		'work': work,
		"carousel": carousel,
	}
	return render(request, 'work.html', context)
