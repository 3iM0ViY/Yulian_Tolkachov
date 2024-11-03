from django.shortcuts import get_object_or_404, render
from .models import *
from Main_n_Settings.models import *
# Create your views here.

def index(request):
	context = {

	}
	return render(request, 'work.html', context)

def work_detail(request, work):
	main = Main.objects.order_by("pk").filter(is_published=True).last()
	sections_list = Section.objects.filter(is_published=True)
	socials_list = Social.objects.filter(is_published=True)

	work = get_object_or_404(Work, is_published = True, slug = work,)
	carousel = CarouselItem.objects.filter(work=work)
	context = {
		"main": main,
		"sections_list": sections_list,
		"socials_list": socials_list,
		'work': work,
		"carousel": carousel,
	}
	return render(request, 'work.html', context)
