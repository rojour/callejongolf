# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
                ('shirt', models.CharField(max_length=4)),
                ('email', models.EmailField(default=b'', max_length=75)),
                ('phone', models.CharField(default=b'', max_length=10)),
                ('comments', models.TextField(default=b'')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
