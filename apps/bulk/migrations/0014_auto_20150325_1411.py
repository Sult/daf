# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0013_auto_20150319_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='executorcorpid',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 14, 11, 53, 950102, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
