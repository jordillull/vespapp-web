# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160414_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='answers',
            field=models.ManyToManyField(blank=True, default=None, related_name='sightings', to='api.Answer', verbose_name='Respuestas'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='source',
            field=models.CharField(max_length=128, verbose_name='Fuente'),
        ),
    ]
