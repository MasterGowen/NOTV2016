# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notvuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]