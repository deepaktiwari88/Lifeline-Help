# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-16 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180315_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='http://www.housingeurope.eu/site/theme/_assets/img/type-article.png', upload_to=''),
        ),
    ]
