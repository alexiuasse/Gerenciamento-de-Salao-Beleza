#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 23/09/2020 14:05.

# Generated by Django 3.1 on 2020-09-23 17:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0010_auto_20200923_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 17, 4, 21, 401473, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='rewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 17, 4, 21, 401473, tzinfo=utc),
                                   verbose_name='Data'),
        ),
    ]
