# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0007_auto_20160526_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(max_length=45, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=45, verbose_name='Last Name')),
                ('groups', models.CharField(choices=[('BKR', 'Booker'), ('ART', 'Artist')], max_length=3, verbose_name='Access')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_photo',
            field=models.ImageField(upload_to='photo'),
        ),
    ]