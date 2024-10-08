from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from Work.models import *
# Create your views here.

def index(request):
	works_list = Work.objects.filter(is_published=True)
	paginator = Paginator(works_list, 5)
	page_number = request.GET.get('page', 1)
	works = paginator.page(page_number)
	
	context = {
		"works": works,
	}
	return render(request, 'index.html', context)