# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mburia', '0005_answer_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer_vote',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='mburia.Mburia_answer'),
        ),
    ]
