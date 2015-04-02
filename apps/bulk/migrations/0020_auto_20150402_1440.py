# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bulk', '0019_auto_20150402_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sovereigntyholder',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 14, 40, 9, 949724, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
