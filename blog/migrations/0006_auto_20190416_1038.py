# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-16 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190416_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(max_length=300, verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.BigIntegerField(blank=True),
        ),
    ]
