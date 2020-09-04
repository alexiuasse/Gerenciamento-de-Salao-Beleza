#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0010_auto_20200904_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrewardretrieved',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
        ),
        migrations.AddField(
            model_name='rewardretrieved',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='historicalrewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 925192, tzinfo=utc),
                                   verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='rewardretrieved',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 14, 25, 56, 925192, tzinfo=utc),
                                   verbose_name='Data'),
        ),
    ]
