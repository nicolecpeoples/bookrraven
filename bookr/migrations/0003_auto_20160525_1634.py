# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 23:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0002_auto_20160525_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='contact_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='booker_id',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]