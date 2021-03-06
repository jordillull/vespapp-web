# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_sightingfaq'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='contact',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='free_text',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Texto sobre localización'),
        ),
        migrations.AlterField(
            model_name='sightingfaq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='faq_images/'),
        ),
    ]
