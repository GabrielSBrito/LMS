# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_gradecurricular_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
            preserve_default=False,
        ),
    ]
