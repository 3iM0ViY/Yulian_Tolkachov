from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor.widgets import CKEditorWidget
from ordered_model.admin import OrderedModelAdmin

from .models import *
# Register your models here.

# ///////////////////////
# Settings admins
# ///////////////////////	

class SectionAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorWidget())
	class Meta():
		model = Section
		fields = "__all__"

# ////////

class MainAdmin(admin.ModelAdmin):
	list_display = ("id", "get_photo", "is_published")
	list_editable = ("is_published",)
	list_display_links = ("id",)
	readonly_fields = ("get_photo",)

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class SectionAdmin(admin.ModelAdmin):
	form = SectionAdminForm
	list_display = ("id", "title", "is_published")
	list_editable = ("title", "is_published")
	list_display_links = ("id",)

class ContactsAdmin(admin.ModelAdmin):
	list_display = ("id", "email", "role", "phone", "is_published")
	search_fields = ("title", "email",)

	def __str__(self):
		return self.title

class SocialAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "is_published")
	list_editable = ("title", "is_published")
	list_display_links = ("id",)

class RequestAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "name", "email", "subject", "created_at")
	search_fields = ("name", "subject", "content",)
	readonly_fields = ("name", "content", "email", "subject", "created_at",)

class MainNSettingsAdminSite(admin.AdminSite):
    site_header = 'Main_N_Settings'
    site_title = 'Main_N_Settings Admin'
    index_title = 'Main_N_Settings'

# ///////////////////////
# Work admins
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

# ///////////////////////

class MainNSettingsAdminSite(admin.AdminSite):
    site_header = 'Main_N_Settings'
    site_title = 'Main_N_Settings Admin'
    index_title = 'Main_N_Settings'

main_n_settings_admin_site = MainNSettingsAdminSite(name='main_n_settings_admin')

main_n_settings_admin_site.register(Main, MainAdmin)
main_n_settings_admin_site.register(Section, SectionAdmin)
main_n_settings_admin_site.register(Contacts, ContactsAdmin)
main_n_settings_admin_site.register(Social, SocialAdmin)
main_n_settings_admin_site.register(Request, RequestAdmin)

class WorkAdminSite(admin.AdminSite):
    site_header = 'Work'
    site_title = 'Work Admin'
    index_title = 'Work'

work_admin_site = WorkAdminSite(name='work_admin')

work_admin_site.register(Work, WorkAdmin)
work_admin_site.register(Photo, PhotoAdmin)