#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0027_auto_20200904_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 830360, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 830414, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 830360, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 830414, tzinfo=utc),
                                   verbose_name='Hora'),
        ),
    ]