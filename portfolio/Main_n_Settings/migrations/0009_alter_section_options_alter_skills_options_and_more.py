# Generated by Django 5.1.1 on 2024-11-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_n_Settings', '0008_section_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order'], 'verbose_name': 'Секція', 'verbose_name_plural': 'Секції'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Скіл', 'verbose_name_plural': 'Скіли'},
        ),
        migrations.AddField(
            model_name='section',
            name='section_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ID секції'),
        ),
    ]