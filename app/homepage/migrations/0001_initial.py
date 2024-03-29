#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/11/2020 11:16.

# Generated by Django 3.1 on 2020-11-08 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=128, verbose_name='Subtítulo')),
                ('address', models.CharField(help_text='Sugestão: Rua, Número, Cidade - Estado, CEP', max_length=255,
                                             verbose_name='Endereço Completo')),
                ('first_image', models.ImageField(blank=True, help_text='Plano de fundo da primeira página.', null=True,
                                                  upload_to='homepage/background/', verbose_name='Primeira Imagem')),
                ('first_video_url',
                 models.CharField(blank=True, help_text='URL do primeiro vídeo, fica no início da página',
                                  max_length=255, null=True, verbose_name='Primeiro Video')),
                ('second_image', models.ImageField(blank=True, help_text='Plano de fundo da página sobre.', null=True,
                                                   upload_to='homepage/background/', verbose_name='Segunda Imagem')),
                ('second_video_url',
                 models.CharField(blank=True, help_text='URL do segundo vídeo, fica na primeira página de sobre',
                                  max_length=255, null=True, verbose_name='Segundo Video')),
                ('whatsapp', models.CharField(help_text='Número do whatsapp', max_length=16, verbose_name='Whatsapp')),
                ('whatsapp_link',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para whatsapp',
                                  max_length=256, verbose_name='Link para whatsapp')),
                ('instagram',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para instagram',
                                  max_length=256, verbose_name='Instagram')),
                ('facebook',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para facebook',
                                  max_length=256, verbose_name='Facebook')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalHomePage',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=128, verbose_name='Subtítulo')),
                ('address', models.CharField(help_text='Sugestão: Rua, Número, Cidade - Estado, CEP', max_length=255,
                                             verbose_name='Endereço Completo')),
                ('first_image',
                 models.TextField(blank=True, help_text='Plano de fundo da primeira página.', max_length=100, null=True,
                                  verbose_name='Primeira Imagem')),
                ('first_video_url',
                 models.CharField(blank=True, help_text='URL do primeiro vídeo, fica no início da página',
                                  max_length=255, null=True, verbose_name='Primeiro Video')),
                ('second_image',
                 models.TextField(blank=True, help_text='Plano de fundo da página sobre.', max_length=100, null=True,
                                  verbose_name='Segunda Imagem')),
                ('second_video_url',
                 models.CharField(blank=True, help_text='URL do segundo vídeo, fica na primeira página de sobre',
                                  max_length=255, null=True, verbose_name='Segundo Video')),
                ('whatsapp', models.CharField(help_text='Número do whatsapp', max_length=16, verbose_name='Whatsapp')),
                ('whatsapp_link',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para whatsapp',
                                  max_length=256, verbose_name='Link para whatsapp')),
                ('instagram',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para instagram',
                                  max_length=256, verbose_name='Instagram')),
                ('facebook',
                 models.CharField(default='https://www.google.com', help_text='Link direcionando para facebook',
                                  max_length=256, verbose_name='Facebook')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical home page',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
