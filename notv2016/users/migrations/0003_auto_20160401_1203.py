# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 07:03
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160401_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notvuser',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=255, verbose_name='Телефон'),
        ),
    ]
