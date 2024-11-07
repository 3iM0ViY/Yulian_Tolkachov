from django.db import models

from ordered_model.models import OrderedModel
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)] #відсоток прогесу

#вибір року
def year_choices():
	return [(r,r) for r in range(1984, datetime.date.today().year+1)]
def current_year():
	return datetime.date.today().year

class Main(models.Model):
	photo = models.ImageField(verbose_name='Фото', upload_to="", blank=True, null=True)
	photo_minified = models.ImageField(verbose_name='Стиснуте фото', upload_to="", null=True, blank=True)
	alt_text = models.CharField(verbose_name="Підпис", max_length=250, blank=True)
	icon = models.ImageField(verbose_name='Іконка', upload_to="", blank=True, null=True)
	cv = models.FileField(upload_to="uploads/", blank=True)
	portfolio_link = models.URLField(verbose_name='Посилання на портфоліо', blank=True, null=True)
	banner = models.ImageField(verbose_name='Банер', upload_to="", blank=True, null=True)
	banner_minified = models.ImageField(verbose_name='Стиснутий банер', upload_to="", null=True, blank=True)
	alt_banner_text = models.CharField(verbose_name="Підпис", max_length=250, null=True, blank=True)
	email = models.EmailField(verbose_name='E-mail', max_length=150, null=True, blank=True)
	role = models.CharField(verbose_name='Посада', max_length=100, null=True, blank=True)
	phone = models.CharField(verbose_name='Телефон', max_length=100, null=True, blank=True)
	signature = models.ImageField(verbose_name='Підпис', upload_to="", blank=True, null=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	class Meta:
		verbose_name = 'Головна сторінка'
		verbose_name_plural = 'Головні сторінки'

class Section(OrderedModel):
	title = models.CharField(verbose_name='Назва', max_length=150)
	slug = models.SlugField(verbose_name='Слаг', max_length=150, null=True)
	subtitle = models.CharField(verbose_name="Підпис", max_length=250, blank=True)
	text = models.TextField(verbose_name='Опис', blank=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Секція'
		verbose_name_plural = 'Секції'
		ordering = ["order"]

class Services(models.Model):
	title = models.CharField(verbose_name='Назва', max_length=150)
	subtitle = models.CharField(verbose_name="Підпис", max_length=250, blank=True)
	photo = models.ImageField(verbose_name='Фото', upload_to="services/", blank=True, null=True)
	photo_minified = models.ImageField(verbose_name='Стиснуте фото', upload_to="services/", null=True, blank=True)
	alt_text = models.CharField(verbose_name="Підпис для фото", max_length=250, null=True, blank=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Сервіс'
		verbose_name_plural = 'Сервіси'
		ordering = ['title']

class Years(models.Model):
	year = models.IntegerField(verbose_name="Рік", choices=year_choices, default=current_year) #вибір року
	content = models.TextField(verbose_name="Вміст", blank=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	def __str__(self):
		return str(self.year) + " рік"

	class Meta:
		verbose_name = 'Рік'
		verbose_name_plural = 'Роки'
		ordering = ['year']

class Skills(models.Model):
	title = models.CharField(verbose_name='Назва', max_length=150)
	percentage = models.PositiveIntegerField(verbose_name='Відсоток', validators=PERCENTAGE_VALIDATOR, default=50) #відсоток прогесу
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Скіл'
		verbose_name_plural = 'Скіли'
		# ordering = ['title']

class Social(models.Model):
	title = models.CharField(verbose_name='Назва', max_length=150)
	url = models.URLField(verbose_name="Посилання", max_length=200)
	icon = models.CharField(verbose_name='Іконка (дві літери)', max_length=5, blank=True, null=True)
	created_at = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	def __str__(self):
		return str(self.title)
	
	class Meta:
		verbose_name = 'Зовнішнє посилання'
		verbose_name_plural = 'Зовішні посилання'
		ordering = ['title']

class Request(models.Model):
	name = models.CharField(max_length=255, verbose_name="Ім'я")
	email = models.EmailField(verbose_name='E-mail', max_length=150, blank=True)
	subject = models.CharField(verbose_name="Тема", max_length=150, blank=True)
	content = models.TextField(verbose_name="Вміст",)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Форма контакту"
		verbose_name_plural = "Форми контакту"
		ordering = ["-created_at"]