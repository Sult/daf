# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20150324_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterjournal',
            name='refid',
        ),
        migrations.AlterField(
            model_name='characterjournal',
            name='amount',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characterjournal',
            name='balance',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characterjournal',
            name='taxamount',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
