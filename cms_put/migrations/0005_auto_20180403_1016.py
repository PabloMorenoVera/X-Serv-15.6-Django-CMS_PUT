# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_put', '0004_page_pagina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pagina',
            field=models.CharField(max_length=128),
        ),
    ]
