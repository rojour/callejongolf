# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='comments',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
