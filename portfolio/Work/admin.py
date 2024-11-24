from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from ordered_model.admin import OrderedModelAdmin

from .models import *

# Register your models here.

class WorkAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditor5Widget())
	class Meta():
		model = Work
		fields = "__all__"

# ///////////////////////

class PhotoInline(admin.TabularInline):
	model = CarouselItem
	extra = 1
	readonly_fields = ("get_photo",)
	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo.photo_minified.url}" width="50">') # об'єкт це посилання на модель з фотографією
		return "-"

	get_photo.short_description = "Фото в ряд"

class PhotoAdmin(admin.ModelAdmin):
	list_display = ("id", "get_photo", "created_at",)
	list_display_links = ("id",)
	list_filter = ("created_at",)
	readonly_fields = ("created_at", "get_photo",)
	show_facets = admin.ShowFacets.ALWAYS

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото окреме"

class WorkAdmin(OrderedModelAdmin):
	inlines = [PhotoInline]
	form = WorkAdminForm
	list_display = ("id", "title", "job", "client", "get_photo", "date_start", "is_main", "is_published")
	list_editable = ("is_main", "is_published",)
	list_display_links = ("id",)
	search_fields = ("title", "subtitle", "job", "client", "content",)
	list_filter = ("is_main", "is_published",)
	prepopulated_fields = {'slug': ('title',)}
	readonly_fields = ("get_photo", "slide")
	fields = ("title", "slug", "subtitle", "photo", "photo_minified", "get_photo", "alt_text", "date_start", "date_end", "client", "job", "content", "is_main", "is_published")
	show_facets = admin.ShowFacets.ALWAYS

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото роботи"

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Work, WorkAdmin)