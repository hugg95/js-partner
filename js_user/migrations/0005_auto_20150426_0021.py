# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_user', '0004_auto_20150426_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsuser',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
