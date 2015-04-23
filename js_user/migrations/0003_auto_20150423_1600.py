# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_user', '0002_jsuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
