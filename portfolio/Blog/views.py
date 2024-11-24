from django.shortcuts import get_object_or_404, render
from .models import *
from Main_n_Settings.models import *
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F

# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'blog.html', context)

def blog_detail(request, blog):
	main = Main.objects.order_by("pk").filter(is_published=True).last()
	sections_list = Section.objects.filter(is_published=True)
	socials_list = Social.objects.filter(is_published=True)

	article = get_object_or_404(Blog, is_published = True, slug = blog,)
	context = {
		"main": main,
		"sections_list": sections_list,
		"socials_list": socials_list,
		'article': article,
	}
	return render(request, 'blog.html', context)

# Так само виводить дописи, тільки класом + готовий лічильник переглядів
class Blog_detail(DetailView):
	model = Blog
	context_object_name = "blog"
	template_name = 'blog.html'

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		self.object.views = F("views") + 1
		self.object.save()
		self.object.refresh_from_db()

		main = Main.objects.order_by("pk").filter(is_published=True).last()
		sections_list = Section.objects.filter(is_published=True)
		socials_list = Social.objects.filter(is_published=True)

		context_extra = {
			"main": main,
			"sections_list": sections_list,
			"socials_list": socials_list,
		}
		context.update(context_extra) # об'єднання двох словників
		return context