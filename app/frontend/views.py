#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 05/09/2020 09:48.

import logging

from config.models import Reward, TypeOfService
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .utils import *

logger = logging.getLogger(__name__)


def error_400(request, exception):
    logger.error("Error 400: [%s]" % exception)
    return render(request, '400.html', {}, status=400)


def error_401(request, exception):
    logger.error("Error 401: [%s]" % exception)
    return render(request, '401.html', {}, status=401)


def error_403(request, exception):
    logger.error("Error 403: [%s]" % exception)
    return render(request, '403.html', {}, status=403)


def error_404(request, exception):
    logger.error("Error 404: [%s]" % exception)
    return render(request, '404.html', {}, status=404)


def error_500(request):
    return render(request, '500.html', {}, status=500)


def error_503(request):
    return render(request, '503.html', {}, status=503)


class HomePage(View):
    template = 'homepage/homepage.html'

    def get(self, request):
        return render(request, self.template, {
            'rewards': Reward.objects.all(),
            'services': TypeOfService.objects.all(),
        })


class Index(View):
    template = 'index.html'

    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('frontend:homepage'))


class Home(LoginRequiredMixin, View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)


class Dashboard(LoginRequiredMixin, View):
    template = 'dashboard.html'

    def get(self, request):
        return render(request, self.template, context_dashboard())


# class Reward(View):
#     template = 'homepage/reward_all.html'
#
#     def get(self, request):
#         return render(request, self.template)


class Chart(LoginRequiredMixin, View):
    template = 'chart.html'

    def get(self, request, year):
        return render(request, self.template, context_chart(year))


class LogoutAdmin(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/admin/')


class LogoutFrontend(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(f'/login/frontend/?next={reverse_lazy("users:customuser:profile_frontend")}')
