# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-01 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='邮箱'),
        ),
    ]
