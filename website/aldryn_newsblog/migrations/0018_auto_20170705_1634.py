# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0017_auto_20170705_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTemplateTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=234, verbose_name='title')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='aldryn_newsblog.ArticleTemplate', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'aldryn_newsblog_articletemplate_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'article template Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='articletemplatetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
