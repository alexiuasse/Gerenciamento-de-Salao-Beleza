#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0016_auto_20200904_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 23, 39, 455466, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='rewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 23, 39, 455466, tzinfo=utc),
                                   verbose_name='Data'),
        ),
    ]
