from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from django.forms import Textarea #розмір поля
from django_ckeditor_5.widgets import CKEditor5Widget
from ordered_model.admin import OrderedModelAdmin

from .models import *
# Register your models here.

class SectionAdminForm(forms.ModelForm):
	text = forms.CharField(widget=CKEditor5Widget())
	class Meta():
		model = Section
		fields = "__all__"

class YearsAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditor5Widget())
	class Meta():
		model = Years
		fields = "__all__"

# ///////////////////////		

class MainAdmin(admin.ModelAdmin):
	list_display = ("id", "get_photo", "email", "role", "phone", "is_published")
	list_editable = ("is_published", "email", "role", "phone",)
	list_display_links = ("id",)
	readonly_fields = ("get_photo",)

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class SectionAdmin(OrderedModelAdmin):
	form = SectionAdminForm
	list_display = ("id", "title", "subtitle", 'order', 'move_up_down_links', "is_published")
	readonly_fields = ('order', 'move_up_down_links',)
	ordering = ('order',)
	list_editable = ("title", "is_published")
	list_display_links = ("id",)

class ServicesAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "subtitle", "get_photo", "is_published")
	list_editable = ("title", "subtitle", "is_published",)
	list_display_links = ("id",)
	readonly_fields = ("get_photo",)

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo_minified.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class YearsAdmin(admin.ModelAdmin):
	form = YearsAdminForm
	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':160})},
    } #розмір поля
	list_display = ("id", "year", "content", "is_published")
	list_editable = ("year", "content", "is_published")
	list_display_links = ("id",)

class SkillsAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "percentage", "is_published")
	list_editable = ("title", "percentage", "is_published")
	list_display_links = ("id",)

class SocialAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "icon", "is_published")
	list_editable = ("title", "icon", "is_published")
	list_display_links = ("id",)

class RequestAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "name", "email", "subject", "created_at")
	search_fields = ("name", "subject", "content",)
	readonly_fields = ("name", "content", "email", "subject", "created_at",)

admin.site.register(Main, MainAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Years, YearsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Request, RequestAdmin)