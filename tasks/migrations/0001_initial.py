# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('task_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasks.Task')),
                ('character', models.BooleanField()),
                ('key', models.IntegerField()),
                ('fromid', models.BigIntegerField(null=True)),
                ('rowcount', models.SmallIntegerField(null=True)),
                ('accountkey', models.SmallIntegerField(null=True)),
            ],
            options={
            },
            bases=('tasks.task',),
        ),
    ]
