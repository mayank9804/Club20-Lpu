# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='Venue',
            field=models.CharField(default='Parade Ground', max_length=250),
        ),
    ]
