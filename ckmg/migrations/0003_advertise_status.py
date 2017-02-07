# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckmg', '0002_remove_advertise_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='status',
            field=models.CharField(default=b'D', max_length=1, choices=[(b'A', b'activate'), (b'D', b'deactivate')]),
            preserve_default=True,
        ),
    ]
