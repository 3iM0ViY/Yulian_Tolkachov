from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва категорії")
	slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Категорія(ю)"
		verbose_name_plural = "Категорії"
		ordering = ["title"]

class Tag(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва тегу")
	slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("tag", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Тег(у)"
		verbose_name_plural = "Теги"
		ordering = ["title"]

class Blog(OrderedModel):
	title = models.CharField(verbose_name='Заголовок', max_length=150)
	slug = models.SlugField(verbose_name='Слаг', max_length=150, null=True)
	subtitle = models.CharField(verbose_name="Підзаголовок", max_length=250, blank=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="Публікації", blank=True, verbose_name="Категорія")
	tags = models.ManyToManyField(Tag, blank=True, related_name="Публікації", verbose_name="Теги")
	content = models.TextField(verbose_name="Вміст", blank=True)
	is_main = models.BooleanField(verbose_name='На головну', default=True)
	is_published = models.BooleanField(verbose_name='Опублікувати', default=True)
	date = models.DateTimeField(verbose_name='Написано', auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Допис'
		verbose_name_plural = 'Дописи'
		ordering = ['-order', '-date', "title"]

	def get_absolute_url(self):
		# return reverse('portfolio:blog_detail', args=[self.slug,])
		return reverse('blog', args=[self.slug,]) # для класа замість вункції views.py