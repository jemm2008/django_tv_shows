# Generated by Django 3.2.6 on 2021-08-20 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01_core', '0002_tv_shows_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv_shows',
            name='release_date',
            field=models.DateField(),
        ),
    ]