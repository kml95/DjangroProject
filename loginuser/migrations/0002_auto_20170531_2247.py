# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfirmation',
            name='code',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
