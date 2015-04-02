# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20150329_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterjournal',
            options={'ordering': ['-date']},
        ),
    ]
