#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 10:03.

# Generated by Django 3.1 on 2020-09-16 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0003_auto_20200916_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 12, 51, 16, 751168, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 16, 12, 51, 16, 751224, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 16, 12, 51, 16, 751168, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 16, 12, 51, 16, 751224, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
    ]