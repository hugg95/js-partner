# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_user', '0003_auto_20150423_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsuser',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
