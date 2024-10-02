from django.db import models
from ordered_model.models import OrderedModel
# Create your models here.

class Main(models.Model):
	photo = models.ImageField(verbose_name='Фото', upload_to="", blank=True, null=True)
	photo_minified = models.ImageField(verbose_name='Стиснуте фото', upload_to="", null=True, blank=True)
	alt_text = models.CharField(verbose_name="Підпис", max_length=250, blank=True)
	icon = models.ImageField(verbose_name='Іконка', upload_to="", blank=True, null=True)
	cv = models.FileField(upload_to="uploads/", blank=True)
	portfolio = models.FileField(upload_to="uploads/", blank=True)
	signature = models.ImageField(verbose_name='Підпис', upload_to="", blank=True, null=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	class Meta:
		verbose_name = 'Головна сторінка'
		verbose_name_plural = 'Головні сторінки'

class Section(models.Model):
	title = models.CharField(verbose_name='Назва', max_length=150)
	subtitle = models.CharField(verbose_name="Підпис для іконки мережі", max_length=250, blank=True)
	text = models.TextField(verbose_name='Опис', blank=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Секція'
		verbose_name_plural = 'Секції'
		ordering = ['title']

class Contacts(models.Model):
	email = models.EmailField(verbose_name='E-mail', max_length=150, blank=True)
	role = models.CharField(verbose_name='Посада', max_length=100, blank=True)
	phone = models.CharField(verbose_name='Телефон', max_length=100, blank=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Контакти'
		verbose_name_plural = 'Контакти'
		ordering = ['email']

class Social(models.Model):
	title = models.CharField(verbose_name='Назва', max_length=150)
	url = models.URLField(verbose_name="Посилання", max_length=200)
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

class Photo(models.Model):
	photo = models.ImageField(verbose_name='Фото', upload_to="work/%Y/%m")
	photo_minified = models.ImageField(verbose_name='Стиснуте фото для мобільних пристроїв', upload_to="work_mini/%Y/%m", null=True, blank=True)
	alt_text = models.CharField(verbose_name="Підпис для фото", max_length=250, null=True, blank=True)
	created_at = models.DateTimeField(verbose_name='Створено', auto_now_add=True, null=True)

	def __str__(self):
		return self.photo.url

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фотографії'
		ordering = ['-created_at']

class Work(OrderedModel):
	title = models.CharField(verbose_name='Заголовок', max_length=150)
	slug = models.SlugField(verbose_name='Слаг', max_length=150, null=True)
	subtitle = models.CharField(verbose_name="Підзаголовок", max_length=250, blank=True)
	photo = models.ImageField(verbose_name='Фото', upload_to="", blank=True, null=True)
	photo_minified = models.ImageField(verbose_name='Стиснуте фото', upload_to="", null=True, blank=True)
	alt_text = models.CharField(verbose_name="Підпис", max_length=250, blank=True)
	date_start = models.DateTimeField(verbose_name='Розпочато', blank=True)
	date_end = models.DateTimeField(verbose_name='Закінчено', blank=True)
	client = models.CharField(verbose_name='Роботодавець', max_length=150, blank=True)
	job = models.CharField(verbose_name='Посада', max_length=150, blank=True,)
	content = models.TextField(verbose_name="Вміст", blank=True)
	slide = models.ManyToManyField(Photo, blank=True, verbose_name="Фото")
	is_main = models.BooleanField(verbose_name='На головну', default=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	updated = models.DateTimeField(auto_now=True, null=True)

	# to do: категорії...

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Проєкт'
		verbose_name_plural = 'Проєкти'
		ordering = ['-order', '-date_end', "title"]

class CarouselItem(models.Model):
	work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name="Робота")
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='Фото карусель')
	order = models.IntegerField(verbose_name='Черга', default=0)
	timestamp = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
	
	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'
		ordering = ['order']