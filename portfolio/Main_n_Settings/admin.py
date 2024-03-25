from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *
# Register your models here.

class SectionAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta():
		model = Section
		fields = "__all__"

# ///////////////////////		

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
	list_display = ("id", "title", "is_published")
	list_editable = ("title", "is_published")
	list_display_links = ("id",)

class ContactsAdmin(admin.ModelAdmin):
	list_display = ("id", "email", "role", "phone", "is_published")
	search_fields = ("title", "email",)

	def __str__(self):
		return self.title

class SocialAdmin(admin.ModelAdmin):
	form = SocialForm
	list_display = ("id", "get_photo", "alt_text", "created_at")
	list_editable = ("alt_text",)
	list_display_links = ("id",)
	readonly_fields = ("created_at", "get_photo")
	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"



class RequestAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "name", "email", "phone", "created_at")
	search_fields = ("name", "content",)
	readonly_fields = ("name", "content", "email", "phone", "created_at",)

class AboutAdmin(admin.ModelAdmin):
	form = AboutAdminForm
	list_display = ("id", "text", "created_at", "is_published")
	search_fields = ("text",)
	readonly_fields = ("created_at",)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ("id", "get_photo", "created_at",)
	list_display_links = ("id",)
	list_filter = ("created_at",)
	readonly_fields = ("created_at", "get_photo",)

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class SingleAdmin(OrderedModelAdmin):
	inlines = [PhotoInline]
	form = SingleAdminForm
	# list_display = ("id", "order", "move_up_down_links", "title", "short_description", "short_description2", "get_photo", "client", "created_at", "is_published")
	list_display = ("id", "move_up_down_links", "title", "short_description", "get_photo", "created_at", "is_published")
	list_editable = ("is_published",)
	list_display_links = ("id",)
	search_fields = ("title", "short_description", "short_description2", "text", "client")
	list_filter = ("is_published",)
	readonly_fields = ("created_at", "get_photo",)
	fields = ("title", "short_description", "short_description2", "photo", "photo_minified", "get_photo", "alt_text", "text", "client", "created_at", "is_published",) #"slide"

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class ServiceAdmin(OrderedModelAdmin):
	form = ServiceAdminForm
	list_display = ("id", "move_up_down_links", "title", "is_published") #'order',
	list_editable = ("is_published", "title")
	list_display_links = ("id",)
	search_fields = ("title", "text")
	list_filter = ("is_published",)

admin.site.register(Main, MainAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Single, SingleAdmin)
admin.site.register(Service, ServiceAdmin)