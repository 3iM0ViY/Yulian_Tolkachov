from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from Work.models import *
from Blog.models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
	main = Main.objects.order_by("pk").filter(is_published=True).last()
	sections_list = Section.objects.filter(is_published=True)
	services_list = Services.objects.filter(is_published=True)
	years_list = Years.objects.order_by("-year").filter(is_published=True)
	skills_list = Skills.objects.filter(is_published=True)
	socials_list = Social.objects.filter(is_published=True)

	works_list = Work.objects.filter(is_published=True)
	paginator = Paginator(works_list, 5)
	page_number = request.GET.get('page', 1)
	works = paginator.page(page_number)

	blog_list = Blog.objects.filter(is_published=True)
	paginator = Paginator(blog_list, 5)
	page_number = request.GET.get('page', 1)
	blogs = paginator.page(page_number)
	
	# обробник форми контакту
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			# Form fields passed validation
			form.cleaned_data.pop("captcha")
			Request.objects.create(**form.cleaned_data)
			messages.success(request, "Your form has been successfully received. Soon I may contact you on the matter.")
			# return redirect("home:home")
		else:
			messages.error(request, "There was an error in your form submission.")
	else:
		form = RequestForm()
	
	context = {
		"main": main,
		"sections_list": sections_list,
		'sections': {section.slug: section for section in sections_list}, # секцій багато, вони розкидані, так можна звертатись по назві
		"services_list": services_list,
		"years_list": years_list,
		"skills_list": skills_list,
		"socials_list": socials_list,
		"works": works,
		"blogs": blogs,
		"form": form,
	}
	return render(request, 'index.html', context)