# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0016_auto_20150325_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='startdate',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 20, 45, 18, 456531, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
