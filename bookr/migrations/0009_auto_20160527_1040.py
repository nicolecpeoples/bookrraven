# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0008_auto_20160527_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='contact_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookr.SomeUser'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookr.SomeUser'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookr.SomeUser'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='booker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookr.SomeUser'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]