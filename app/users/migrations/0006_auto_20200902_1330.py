#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/09/2020 19:50.

# Generated by Django 3.1 on 2020-09-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_auto_20200824_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='total_of_points',
            field=models.IntegerField(default=0, verbose_name='Total de pontos'),
        ),
    ]