# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150817_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='user',
        ),
    ]
