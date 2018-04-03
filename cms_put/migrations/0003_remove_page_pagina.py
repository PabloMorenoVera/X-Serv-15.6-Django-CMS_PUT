# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_put', '0002_auto_20180403_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='pagina',
        ),
    ]
