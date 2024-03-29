from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *
# Register your models here.

class SectionAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditorWidget())
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

admin.site.register(Main, MainAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Request, RequestAdmin)