# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySiteMain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyToComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe7\xa7\xb0\xe5\x91\xbc')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('content', models.CharField(max_length=140, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('replytime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x97\xb6\xe9\x97\xb4')),
                ('comment', models.ForeignKey(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba', to='MySiteMain.Comment')),
            ],
        ),
    ]
