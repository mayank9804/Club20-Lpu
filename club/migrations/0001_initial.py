# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 18:05
from __future__ import unicode_literals

import club.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessfullEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('details', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='SuccessfullEventsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snap', models.ImageField(upload_to=club.models.SuccessfullEventsImages.upload_path)),
                ('successfullevents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SuccessfullEvents', to='club.SuccessfullEvents')),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('details', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('slug', models.SlugField()),
                ('poster', models.ImageField(upload_to=club.models.UpcomingEvents.get_upload_path)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
