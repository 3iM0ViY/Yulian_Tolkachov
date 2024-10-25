from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
	# path('', index, name = "portfolio"),
	path('<slug:work>/', work_detail, name='work_detail'),
]