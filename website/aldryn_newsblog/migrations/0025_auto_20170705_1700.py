# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0024_auto_20170705_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletemplate',
            options={'verbose_name': 'Article Template'},
        ),
        migrations.AlterModelOptions(
            name='articletemplatetranslation',
            options={'default_permissions': (), 'verbose_name': 'Article Template Translation', 'managed': True},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_template',
            field=models.ForeignKey(verbose_name='Article Template', blank=True, to='aldryn_newsblog.ArticleTemplate', null=True),
        ),
    ]
