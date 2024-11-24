from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from ordered_model.admin import OrderedModelAdmin

from .models import *
# Register your models here.

class BlogAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditor5Widget())
	class Meta():
		model = Blog
		fields = "__all__"

class BlogAdmin(OrderedModelAdmin):
	form = BlogAdminForm
	list_display = ("id", "title", "subtitle", "category", "date", "is_main", "is_published")
	list_editable = ("title", "subtitle", "category", "is_main", "is_published",)
	list_display_links = ("id",)
	search_fields = ("title", "subtitle", "category", "tags", "content",)
	list_filter = ("category", "tags", "is_main", "is_published",)
	prepopulated_fields = {'slug': ('title',)}
	readonly_fields = ("date",)
	fields = ("title", "slug", "subtitle", "category", "tags", "date", "content", "is_main", "is_published")
	show_facets = admin.ShowFacets.ALWAYS

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)