# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0034_auto_20170705_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogfeaturedarticlesplugin',
            name='skip_articles',
            field=models.PositiveIntegerField(default=0, help_text='Amout of featured articles to Skip.', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='newsbloglatestarticlesplugin',
            name='skip_articles',
            field=models.PositiveIntegerField(default=0, help_text='Amout of lastest articles to Skip.', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='newsblogarchiveplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsblogarticlesearchplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsblogauthorsplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsblogcategoriesplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsblogfeaturedarticlesplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsbloglatestarticlesplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
        migrations.AlterField(
            model_name='newsblogtagsplugin',
            name='custom_template',
            field=models.CharField(blank=True, max_length=255, choices=[(b'small', b'Small Image Format')]),
        ),
    ]
