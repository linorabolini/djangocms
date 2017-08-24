# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0033_auto_20170705_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsblogfeaturedarticlesplugin',
            old_name='article_template',
            new_name='custom_template',
        ),
        migrations.RenameField(
            model_name='newsbloglatestarticlesplugin',
            old_name='article_template',
            new_name='custom_template',
        ),
        migrations.RemoveField(
            model_name='newsblogrelatedplugin',
            name='article_template',
        ),
        migrations.AddField(
            model_name='newsblogarchiveplugin',
            name='custom_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[(b'default', b'Default')]),
        ),
        migrations.AddField(
            model_name='newsblogarticlesearchplugin',
            name='custom_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[(b'default', b'Default')]),
        ),
        migrations.AddField(
            model_name='newsblogauthorsplugin',
            name='custom_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[(b'default', b'Default')]),
        ),
        migrations.AddField(
            model_name='newsblogcategoriesplugin',
            name='custom_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[(b'default', b'Default')]),
        ),
        migrations.AddField(
            model_name='newsblogtagsplugin',
            name='custom_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[(b'default', b'Default')]),
        ),
    ]
