# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20160304_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cadre',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='local_government',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
