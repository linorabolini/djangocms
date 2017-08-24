# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0027_auto_20170705_1703'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articletemplatetranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='articletemplatetranslation',
            name='master',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_template',
            field=models.CharField(default='', max_length=255, choices=[('', 'Default')]),
        ),
        migrations.DeleteModel(
            name='ArticleTemplate',
        ),
        migrations.DeleteModel(
            name='ArticleTemplateTranslation',
        ),
    ]
