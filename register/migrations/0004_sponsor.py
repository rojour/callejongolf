# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150327_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cont_first_name', models.CharField(max_length=15)),
                ('cont_last_name', models.CharField(max_length=20)),
                ('cont_email', models.EmailField(default=b'', max_length=75)),
                ('cont_phone', models.CharField(default=b'', max_length=12)),
                ('cont_comments', models.TextField(default=b'', null=True, blank=True)),
                ('sponsor_name', models.CharField(max_length=20)),
                ('sponsor_type', models.CharField(max_length=10)),
                ('sponsor_pay_status', models.CharField(max_length=10, null=True, blank=True)),
                ('sponsor_pay_method', models.CharField(max_length=15, null=True, blank=True)),
                ('sponsor_created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
