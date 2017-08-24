# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0021_auto_20170705_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletemplatetranslation',
            name='title',
            field=models.CharField(default='', max_length=234, null=True, verbose_name='title', blank=True),
        ),
    ]
