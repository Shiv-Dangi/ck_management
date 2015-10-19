# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advertise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advertiser_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'Images/Advertisement')),
                ('html_link', models.CharField(default=b'https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkcmNoaXRyYWRoYXdhbGV8Z3g6NDQzYzkwN2Y3YzY2ZWRjYw', max_length=200)),
                ('status', models.CharField(default=b'D', max_length=1, choices=[(b'A', b'activate'), (b'D', b'deactivate')])),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=2011, max_length=4)),
                ('student_name', models.CharField(max_length=50)),
                ('college_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='buisness_plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buisness_title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to=b'Docs/buisness_plan/pdf')),
                ('ppt_file', models.FileField(upload_to=b'Docs/buisness_plan/ppt')),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_no', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(regex=b'^.{10}$', message=b'Mobile no has to be 10 digits long', code=b'nomatch')])),
                ('message', models.TextField(max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='modelpaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelpaper_title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to=b'Docs/Model_Paper/pdf')),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_title', models.CharField(max_length=100)),
                ('link', models.CharField(default=b'https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxkcmNoaXRyYWRoYXdhbGV8Z3g6NDQzYzkwN2Y3YzY2ZWRjYw', max_length=200)),
                ('date', models.DateField()),
                ('news_type', models.CharField(default=b'MN', max_length=3, choices=[(b'MN', b'Marketing News'), (b'HRN', b'HR News'), (b'FN', b'Finance News'), (b'CO', b'Current Opening')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ppt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ppt_title', models.CharField(max_length=100)),
                ('ppt_file', models.FileField(upload_to=b'Docs/PPT/ppt')),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_title', models.CharField(max_length=100)),
                ('doc_file', models.FileField(upload_to=b'Docs/project/docfile')),
                ('pdf_file', models.FileField(upload_to=b'Docs/project/pdf')),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=2011, max_length=4)),
                ('student_name', models.CharField(max_length=50)),
                ('college_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_catagary', models.CharField(default=b'MR', max_length=3, choices=[(b'CoS', b'Core Subject'), (b'MR', b'Marketing'), (b'FA', b'Finance'), (b'HR', b'Human Resource')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='theorynotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes_title', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to=b'Docs/Theory_Notes/pdf')),
                ('ppt_file', models.FileField(upload_to=b'Docs/Theory_Notes/ppt')),
                ('date', models.DateField()),
                ('subject', models.ForeignKey(to='ckmg.subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ppt',
            name='subject',
            field=models.ForeignKey(to='ckmg.subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='modelpaper',
            name='subject',
            field=models.ForeignKey(to='ckmg.subject'),
            preserve_default=True,
        ),
    ]
