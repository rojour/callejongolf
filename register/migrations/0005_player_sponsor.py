# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sponsor',
            field=models.ForeignKey(default='', null=True , to='register.Sponsor'),
            preserve_default=False,
        ),
    ]
