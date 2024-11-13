from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
	# можна й так і так, але класом має бути трошки краще
	# path("<str:blog>/", blog_detail, name="blog_detail"),
	path("<str:slug>/", Blog.as_view(), name="blog_detail"),
]