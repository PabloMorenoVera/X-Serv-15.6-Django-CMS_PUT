# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_put', '0003_remove_page_pagina'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='pagina',
            field=models.TextField(default=10000000000),
            preserve_default=False,
        ),
    ]
