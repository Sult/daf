# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='characterjournal',
            unique_together=set([('characterapi', 'date', 'balance')]),
        ),
    ]
