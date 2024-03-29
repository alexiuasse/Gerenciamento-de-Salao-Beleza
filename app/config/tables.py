#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 16/09/2020 11:08.
from django.utils.safestring import mark_safe
from django_tables2 import tables, TemplateColumn, Column

from .models import *


class TypeOfPaymentTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = TypeOfPayment
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name']


class RewardTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Reward
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'quantity_in_points', 'contextual', 'available', 'image', 'description']

    @staticmethod
    def render_quantity_in_points(value):
        return f'{value} pts'

    @staticmethod
    def render_available(value):
        return "Disponível" if value else "Indisponível"

    @staticmethod
    def render_contextual(value):
        return mark_safe(f"<span class='badge' style='background-color: {value}'>{value}</span>")

    @staticmethod
    def render_description(value):
        return f"{value[:18]} ..."


class TypeOfServiceTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = TypeOfService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual', 'value', 'time', 'rewarded_points', 'image', 'description']

    @staticmethod
    def render_rewarded_points(value):
        return f'{value} pts'

    @staticmethod
    def render_value(value):
        return f"R$ {value}"

    @staticmethod
    def render_time(value):
        return f"{value} min"

    @staticmethod
    def render_contextual(value):
        return mark_safe(f"<span class='badge' style='background-color: {value}'>{value}</span>")

    @staticmethod
    def render_description(value):
        return f"{value[:18]} ..."


class StatusServiceTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusService
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']

    @staticmethod
    def render_contextual(value):
        return mark_safe(f"<span class='badge' style='background-color: {value}'>{value}</span>")


class StatusPaymentTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = StatusPayment
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'contextual']

    @staticmethod
    def render_contextual(value):
        return mark_safe(f"<span class='badge' style='background-color: {value}'>{value}</span>")


class ExpedientTable(tables.Table):
    name = Column(linkify=lambda record: record.get_edit_url())
    time = Column(accessor='get_business_hours', verbose_name='Tempo')
    _ = TemplateColumn(template_name='base/table/buttons.html')

    class Meta:
        model = Expedient
        attrs = {'class': 'table table-striped table-hover'}
        per_page = 10
        fields = ['name', 'start_time', 'end_time', 'time']

    @staticmethod
    def render_time(value):
        return mark_safe(f"{value} min")
