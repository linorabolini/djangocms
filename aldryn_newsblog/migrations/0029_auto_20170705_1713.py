# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0028_auto_20170705_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_template',
            field=models.CharField(default='default', max_length=255, choices=[('default', 'Default')]),
        ),
    ]
