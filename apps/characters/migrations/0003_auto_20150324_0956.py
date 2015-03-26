# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20150323_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterjournal',
            name='taxamount',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characterjournal',
            name='taxreceiverid',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='characterjournal',
            unique_together=set([('characterapi', 'refid')]),
        ),
    ]
