#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 27/08/2020 17:26.

# Generated by Django 3.1 on 2020-08-27 20:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0009_auto_20200827_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaltypeofservice',
            old_name='contextutal',
            new_name='contextual',
        ),
        migrations.RenameField(
            model_name='typeofservice',
            old_name='contextutal',
            new_name='contextual',
        ),
    ]