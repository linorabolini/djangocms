# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0022_auto_20170705_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='aldryn_newsblog.ArticleTemplate', null=True),
        ),
    ]
