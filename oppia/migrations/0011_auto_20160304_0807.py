# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0010_auto_20151026_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='facility_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='staff_id',
        ),
    ]
