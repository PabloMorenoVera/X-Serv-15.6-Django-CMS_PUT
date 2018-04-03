# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_put', '0005_auto_20180403_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pagina',
            new_name='dir_acortada',
        ),
    ]
