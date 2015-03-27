# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150326_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='group_play',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='pay_method',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='pay_status',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='phone',
            field=models.CharField(default=b'', max_length=12),
            preserve_default=True,
        ),
    ]
