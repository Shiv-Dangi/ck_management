# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckmg', '0005_auto_20151120_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='year',
            field=models.IntegerField(default=2011),
        ),
    ]
