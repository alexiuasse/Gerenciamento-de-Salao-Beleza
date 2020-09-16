#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 11:00.

from datetime import datetime

# users/models.py
from base.models import BaseModel
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class RewardRetrieved(BaseModel):
    reward = models.ForeignKey("config.Reward", on_delete=models.PROTECT, verbose_name="Brinde")
    points = models.IntegerField("Pontos", default=0)
    quantity = models.IntegerField("Quantidade", default=1)
    date = models.DateField("Data", default=timezone.localtime(timezone.now()))
    retrieved = models.BooleanField("Resgatado", default=False, help_text="Esse brinde já foi resgatado?")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")

    def __str__(self):
        return f"{self.reward} de {self.customer}"

    @property
    def get_absolute_url(self):
        return self.customer.profile.get_back_url_child_admin()

    @property
    def get_delete_url(self):
        return reverse('users:rewardretrieved:delete', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('users:rewardretrieved:edit', kwargs={'cpk': self.customer.pk, 'pk': self.pk})

    @property
    def get_back_url(self):
        return self.customer.profile.get_back_url_child_admin()

    @property
    def get_confirm_url(self):
        return reverse('users:rewardretrieved:confirm', kwargs={'pk': self.pk})

    def get_retrieved_html(self):
        return "Resgatado" if self.retrieved else "Não Resgatado"


class Profile(BaseModel):
    name = models.CharField("nome completo", max_length=150)
    birth_date = models.DateField('data de nascimento', blank=True, null=True, help_text="Informe uma data válida!")
    whatsapp = models.CharField('whatsapp', max_length=16, help_text="Esse será o número usado para contato!")
    total_of_points = models.IntegerField(default=0, verbose_name='Total de pontos')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    @property
    def get_new_service_url(self):
        return reverse('service:orderofservice:create', kwargs={'cpk': self.pk})

    @property
    def get_new_service_url_frontend(self):
        return reverse('service:orderofservice:create_frontend')

    @property
    def get_new_reward_url(self):
        return reverse('users:rewardretrieved:create', kwargs={'cpk': self.pk})

    def get_absolute_url(self):
        return reverse('users:admin:profile', kwargs={'pk': self.pk})

    @property
    def get_delete_url(self):
        return reverse('users:admin:delete', kwargs={'pk': self.pk})

    @property
    def get_edit_url(self):
        return reverse('users:admin:edit', kwargs={'pk': self.pk})

    def get_back_url_child_admin(self):
        return reverse('users:admin:profile', kwargs={'pk': self.pk})

    @property
    def get_back_url(self):
        return reverse('users:admin:view')

    @property
    def get_edit_url_frontend(self):
        return reverse('users:frontend:update')

    def is_birthday(self):
        today = datetime.today()
        return self.birth_date.day == today.day and self.birth_date.month == today.month if self.birth_date else False

    def get_age(self):
        return datetime.today().year - self.birth_date.year

    def get_birth_day_data(self):
        return {
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
        }

    def get_dict_data(self):
        return {
            'Usuário': self.user.username,
            'Nome': self.get_full_name(),
            'Whatsapp': self.whatsapp,
            'Data de Nascimento': self.birth_date,
            'E-mail': self.user.email,
        }

    def get_dict_data_points(self):
        return {
            'Total de Pontos': self.total_of_points,
        }

    def has_service(self):
        return self.user.orderofservice_set.count()

    def get_service_sorted_by_entry_date(self):
        retDict = {}
        for s in self.user.orderofservice_set.all().order_by('-date', '-id'):
            m_y = "{}/{}".format(s.date.month, s.date.year)
            if m_y in retDict:
                retDict[m_y]['services'].append(s)
            else:
                retDict[m_y] = {}
                retDict[m_y]['services'] = []
                retDict[m_y]['services'].append(s)
        return retDict

    def get_service_sorted_by_actual_month(self):
        # retDict = {}
        # for s in self.orderofservice_set.filter(date__month=datetime.today().month).order_by('-date', '-id'):
        #     m_y = "{}/{}".format(s.date.month, s.date.year)
        #     if m_y in retDict:
        #         retDict[m_y]['services'].append(s)
        #     else:
        #         retDict[m_y] = {}
        #         retDict[m_y]['services'] = []
        #         retDict[m_y]['services'].append(s)
        # # print(retDict)
        # return retDict
        return self.user.orderofservice_set.all().order_by('-id')[:5]

    def has_reward(self):
        return self.user.rewardretrieved_set.count()

    def sorted_reward_set(self):
        return self.user.rewardretrieved_set.order_by('-date', '-id')[:5]
