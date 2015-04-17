# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_player_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sponsor',
            field=models.ForeignKey(blank=True, to='register.Sponsor', null=True),
            preserve_default=True,
        ),
    ]
