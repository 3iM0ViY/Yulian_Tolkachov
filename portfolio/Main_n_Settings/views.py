from django.contrib.admin import AdminSite
from django.shortcuts import render
from django.urls import path
from .admin import main_n_settings_admin_site, work_admin_site
from .models import *
# Create your views here.

def index(request):
	context = {

	}
	return render(request, 'index.html', context)

def work(request):
	context = {

	}
	return render(request, 'work.html', context)

def blog(request):
	context = {

	}
	return render(request, 'blog.html', context)

def custom_admin_index(request):
    main_n_settings_app_list = main_n_settings_admin_site.get_app_list(request)
    work_app_list = work_admin_site.get_app_list(request)
    
    print("Main_N_Settings App List:", main_n_settings_app_list)
    print("Work App List:", work_app_list)
    
    context = {
        'app_list': AdminSite().get_app_list(request),
        'main_n_settings_app_list': main_n_settings_app_list,
        'work_app_list': work_app_list,
    }
    return render(request, 'admin/index.html', context)
