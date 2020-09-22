#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 21/09/2020 21:42.

# Generated by Django 3.1 on 2020-09-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=128, null=True)),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('show', models.BooleanField(default=True)),
                ('important', models.BooleanField(default=False)),
            ],
        ),
    ]
