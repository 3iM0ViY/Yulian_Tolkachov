# Generated by Django 5.1.1 on 2024-09-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_n_Settings', '0002_alter_section_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='role',
            field=models.CharField(blank=True, max_length=100, verbose_name='Посада'),
        ),
    ]