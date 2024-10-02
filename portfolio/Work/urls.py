from django.urls import path
from .views import *

app_name = 'work'

urlpatterns = [
	path('', work),
	# path('<int:id>/', post_detail, name='post_detail'),
]