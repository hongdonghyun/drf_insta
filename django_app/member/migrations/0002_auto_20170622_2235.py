# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]