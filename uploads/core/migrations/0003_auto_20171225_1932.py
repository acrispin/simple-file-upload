# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'managed': True, 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
