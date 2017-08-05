# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0025_auto_20170705_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletemplatetranslation',
            name='slug',
            field=models.SlugField(default='', max_length=255, blank=True, help_text='Leave blank to auto-generate a unique slug.', verbose_name='unique slug'),
        ),
    ]
