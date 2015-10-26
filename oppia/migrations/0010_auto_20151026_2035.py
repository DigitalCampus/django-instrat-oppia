# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0009_auto_20150524_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facility_name',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='staff_id',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
