# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-01 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
            ],
        ),
    ]
