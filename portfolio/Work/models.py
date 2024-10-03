from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse
# Create your models here.

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

	def get_absolute_url(self):
		return reverse('portfolio:work_detail', args=[self.slug,])

class CarouselItem(models.Model):
	work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name="Робота")
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE, verbose_name='Фото карусель')
	order = models.IntegerField(verbose_name='Черга', default=0)
	timestamp = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
	
	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'
		ordering = ['order']