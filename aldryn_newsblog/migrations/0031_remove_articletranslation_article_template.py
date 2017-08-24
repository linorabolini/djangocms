# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0030_auto_20170705_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletranslation',
            name='article_template',
        ),
    ]
