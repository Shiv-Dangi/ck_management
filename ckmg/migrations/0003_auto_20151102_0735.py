# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckmg', '0002_auto_20151102_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness_plan',
            name='buisnessplan_desc',
            field=models.TextField(default=b'Buisness Plan Describtion', max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_desc',
            field=models.TextField(default=b'Project Describtion', max_length=5000),
        ),
    ]
