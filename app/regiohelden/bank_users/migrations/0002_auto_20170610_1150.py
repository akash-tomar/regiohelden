# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IBANDetails',
            new_name='IBANDetail',
        ),
    ]
