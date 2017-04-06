# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['display_order'], 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='display_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]