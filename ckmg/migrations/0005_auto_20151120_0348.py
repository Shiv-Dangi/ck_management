# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckmg', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='year',
            field=models.IntegerField(default=2011),
        ),
    ]
