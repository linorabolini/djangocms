# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0026_articletemplatetranslation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletemplatetranslation',
            name='title',
            field=models.CharField(default='', max_length=234, verbose_name='title', blank=True),
        ),
    ]
