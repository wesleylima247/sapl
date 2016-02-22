# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0010_auto_20160216_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normajuridica',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
