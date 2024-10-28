# Generated by Django 5.1.1 on 2024-10-28 17:38

import Main_n_Settings.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_n_Settings', '0005_alter_social_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Підпис')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Фото')),
                ('photo_minified', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Стиснуте фото')),
                ('alt_text', models.CharField(blank=True, max_length=250, null=True, verbose_name='Підпис для фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опублікувати')),
            ],
            options={
                'verbose_name': 'Сервіс',
                'verbose_name_plural': 'Сервіси',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва')),
                ('percentage', models.PositiveIntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Відсоток')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опублікувати')),
            ],
            options={
                'verbose_name': 'Скіл',
                'verbose_name_plural': 'Скіли',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=Main_n_Settings.models.year_choices, default=Main_n_Settings.models.current_year, verbose_name='Рік')),
                ('content', models.TextField(blank=True, verbose_name='Вміст')),
            ],
            options={
                'verbose_name': 'Рік',
                'verbose_name_plural': 'Роки',
                'ordering': ['year'],
            },
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.AddField(
            model_name='main',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='main',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='main',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='section',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250, verbose_name='Підпис'),
        ),
    ]