# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 11:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='IBANDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countrycode', models.CharField(max_length=2)),
                ('checksum', models.CharField(max_length=2)),
                ('swiftcode', models.CharField(max_length=4)),
                ('accountnumber', models.CharField(max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name='bankuser',
            name='iban',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_user', to='bank_users.IBANDetails'),
        ),
        migrations.AddField(
            model_name='bankuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
