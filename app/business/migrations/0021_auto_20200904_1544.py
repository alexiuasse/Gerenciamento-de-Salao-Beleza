#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 04/09/2020 17:20.

# Generated by Django 3.1 on 2020-09-04 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('business', '0020_auto_20200904_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 834614, tzinfo=utc),
                                   help_text='Caso selecionado vários dias, deixe como está!', verbose_name='dia'),
        ),
        migrations.AlterField(
            model_name='historicalbusinessday',
            name='day',
            field=models.DateField(default=datetime.datetime(2020, 9, 4, 18, 44, 27, 834614, tzinfo=utc),
                                   help_text='Caso selecionado vários dias, deixe como está!', verbose_name='dia'),
        ),
    ]
