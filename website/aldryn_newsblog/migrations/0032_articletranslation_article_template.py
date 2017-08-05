# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0031_remove_articletranslation_article_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletranslation',
            name='article_template',
            field=models.CharField(default='default', max_length=255, blank=True, choices=[('default', 'Default')]),
        ),
    ]
