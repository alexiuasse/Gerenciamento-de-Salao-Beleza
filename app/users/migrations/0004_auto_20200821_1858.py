#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/08/2020 19:09.

# Generated by Django 3.1 on 2020-08-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20200821_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='whatsapp',
            field=models.CharField(max_length=16, verbose_name='whatsapp'),
        ),
    ]
