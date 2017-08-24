# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0023_auto_20170705_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_template',
            field=models.ForeignKey(verbose_name='article template', blank=True, to='aldryn_newsblog.ArticleTemplate', null=True),
        ),
    ]
