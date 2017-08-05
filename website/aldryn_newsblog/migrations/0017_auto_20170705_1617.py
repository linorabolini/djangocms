# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0016_auto_20170705_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_new',
        ),
        migrations.AddField(
            model_name='article',
            name='article_template',
            field=models.ForeignKey(default='', to='aldryn_newsblog.ArticleTemplate'),
            preserve_default=False,
        ),
    ]
