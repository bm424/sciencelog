# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('opened', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=128)),
                ('discussion', models.TextField(blank=True)),
                ('shelved', models.BooleanField(default=False)),
                ('related',
                 models.ManyToManyField(blank=True, to='logger.Investigation')),
            ],
        ),
    ]
