#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/09/2020 11:04.
from typing import Dict, Any

from config.models import TypeOfService
from django.contrib.admin.utils import NestedObjects
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, DeleteView
from frontend.icons import ICON_CALENDAR
from service.models import OrderOfService

from .conf import *
from .forms import *
from .models import *
from .utils import *


########################################################################################################################


@login_required
@require_http_methods(["GET"])
def get_calendar_data_frontend(request):
    start = datetime.datetime.strptime(request.GET.get('start', None), "%Y-%m-%dT%H:%M:%SZ")
    end = datetime.datetime.strptime(request.GET.get('end', None), "%Y-%m-%dT%H:%M:%SZ")
    data = []
    businessday = BusinessDay.objects.filter(day__range=[start, end])
    for b in businessday:
        if b.get_is_full() or b.force_day_full:
            className = 'dayfull'
        elif not b.is_work_day:
            className = 'notworkday'
        else:
            className = 'daynotfull'
        data.append({
            'isFull': 'true',
            'start': b.get_start_date_time(),
            'end': b.get_end_date_time(),
            'allDay': 'true',
            'display': 'background',
            'className': className,
        })
    return JsonResponse({'data': data})


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('business.view_businessday', 'service.view_orderofservice', raise_exception=True)
def get_calendar_data_admin(request):
    data = []
    if request.user.is_superuser:
        start = datetime.datetime.strptime(request.GET.get('start', None), "%Y-%m-%dT%H:%M:%SZ")
        end = datetime.datetime.strptime(request.GET.get('end', None), "%Y-%m-%dT%H:%M:%SZ")
        orderofservices = OrderOfService.objects.filter(date__range=[start, end])
        for s in orderofservices:
            data.append({
                'type': 0,
                'pk': s.pk,
                'title': s.get_name_html() if not s.canceled else 'CANCELADO',
                'start': f"{s.date}T{s.time}",
                'url': s.get_absolute_url(),
                'color': s.type_of_service.contextual,
                'display': 'block',
                'className': 'check' if s.get_contextual() else '',
            })
        businessday = BusinessDay.objects.filter(day__range=[start, end])
        for b in businessday:
            if b.is_work_day:
                data.append({
                    'type': 1,
                    'pk': b.pk,
                    'title': b.get_name_html(),
                    'start': b.get_start_date_time(),
                    'end': b.get_end_date_time(),
                    'url': b.get_absolute_url(),
                    'color': b.color,
                    'display': 'block',
                })
            if b.get_is_full():
                className = 'dayfull'
            elif b.force_day_full:
                className = 'forcedayfull'
            elif not b.is_work_day:
                className = 'notworkday'
            else:
                className = 'daynotfull'
            data.append({
                'isFull': 'true',
                'start': b.get_start_date_time(),
                'end': b.get_end_date_time(),
                'allDay': 'true',
                'display': 'background',
                'className': className,
            })
    return JsonResponse({'data': data})


########################################################################################################################

@login_required
@require_http_methods(["GET"])
def businessday_get_hours(request, pk, bpk):
    """
    Check if a Type Of Service fit in the businessday, called from client schedule service
    :param request:
    :param pk: type of service
    :param bpk: bussinesday
    :return: JsonResponse with the hours, Empty if not exists
    """
    type_of_service = get_object_or_404(TypeOfService, pk=pk)
    slices = type_of_service.time / settings.SLICE_OF_TIME  # how many slices is need for this service
    businessday = get_object_or_404(BusinessDay, pk=bpk)
    data = businessday.get_tuple_remain_hours()
    if slices > 1:
        # for each available hours, check if service fit in there, if not remove it
        # the service MUST fit sequentially
        remain_hours = businessday.get_remain_hours_list()  # list of remain hours
        tupple_hours = []
        # check if is consecutive
        for rh in remain_hours:
            start = rh
            end = (rh + datetime.timedelta(minutes=type_of_service.time))
            # hours that the service need
            h_list = datetime_range(start, end, datetime.timedelta(minutes=settings.SLICE_OF_TIME))
            f = True  # add this time?
            for h in h_list:
                if h not in remain_hours:
                    f = False
            if f:
                tupple_hours.append((rh.strftime('%H:%M'), rh.strftime('%H:%M')))
        data = tupple_hours

    return JsonResponse(
        data=data,
        safe=False
    )


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('business.create_businessday', 'business.edit_businessday', raise_exception=True)
def businessday_create(request):
    """
    Create businessday getting the start and end date from request and the rest from form, called from calendar admin
    :param request:
    :return: redirect to page
    """
    form = BusinessDayForm(request.POST)
    if form.is_valid():
        start = datetime.datetime.strptime(form['start'].value(), "%Y-%m-%d")
        end = datetime.datetime.strptime(form['end'].value(), "%Y-%m-%d")
        with transaction.atomic():
            dates = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
            for d in dates:
                try:
                    instance = BusinessDay.objects.get(day=d)
                    instance.color = form['color'].value()
                    instance.is_work_day = form['is_work_day'].value()
                    instance.force_day_full = form['force_day_full'].value()
                    instance.save()
                    instance.expedient_day.clear()
                    instance.expedient_day.add(*form['expedient_day'].value())
                except BusinessDay.DoesNotExist:
                    instance = BusinessDay(
                        day=d,
                        color=form['color'].value(),
                        is_work_day=form['is_work_day'].value(),
                        force_day_full=form['force_day_full'].value(),
                    )
                    instance.save()
                    instance.expedient_day.add(*form['expedient_day'].value())
    return redirect('business:admin:calendar')


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('business.view_businessday', raise_exception=True)
def business_calendar(request):
    return render(request, 'business/calendar.html', {
        'config': {
            'title': {
                'text': TITLE_VIEW_CALENDAR,
                'icon': ICON_CALENDAR
            },
            'pre_title': SUBTITLE_CALENDAR,
        },
        'start_date': datetime.datetime.today().date,
        'form': BusinessDayForm(),
    })


@login_required
@staff_member_required()
@require_http_methods(["GET"])
@permission_required('business.view_businessday', raise_exception=True)
def business_profile(request, pk):
    return render(request, 'business/profile.html', {'obj': BusinessDay.objects.get(pk=pk)})


class BusinessDayEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BusinessDay
    form_class = BusinessDayForm
    template_name = 'business/form.html'
    permission_required = 'business.edit_businessday'
    title = TITLE_EDIT_BUSINESS_DAY
    subtitle = SUBTITLE_BUSINESS_DAY


class BusinessDayDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BusinessDay
    template_name = "business/confirm_delete.html"
    permission_required = 'business.del_businessday'
    title = TITLE_EDIT_BUSINESS_DAY
    subtitle = SUBTITLE_BUSINESS_DAY

    def get_success_url(self):
        return reverse_lazy('business:admin:calendar')

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context

########################################################################################################################
