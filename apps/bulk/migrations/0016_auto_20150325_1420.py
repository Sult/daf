# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0015_auto_20150325_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='name',
            field=models.CharField(unique=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 14, 20, 49, 809236, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
