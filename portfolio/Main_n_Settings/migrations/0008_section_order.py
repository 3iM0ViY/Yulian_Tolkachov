# Generated by Django 5.1.1 on 2024-10-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_n_Settings', '0007_years_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]