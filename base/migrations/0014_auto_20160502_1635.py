# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_problemamigracao_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemamigracao',
            name='descricao',
            field=models.CharField(default='', max_length=300, verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problemamigracao',
            name='problema',
            field=models.CharField(default='', max_length=300, verbose_name='Problema'),
            preserve_default=False,
        ),
    ]
