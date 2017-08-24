# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0029_auto_20170705_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_template',
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='article_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[('default', 'Default')]),
        ),
    ]
