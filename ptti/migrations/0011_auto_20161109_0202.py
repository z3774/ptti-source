# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptti', '0010_auto_20161109_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntatestti',
            name='numero',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testti',
            name='no_preguntas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]