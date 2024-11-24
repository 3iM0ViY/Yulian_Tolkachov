from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
	# можна й так і так, але класом має бути трошки краще
	path("<str:slug>/", Blog_detail.as_view(), name="Blog_detail"),
	# path("<str:blog>/", blog_detail, name="blog_detail"),
]