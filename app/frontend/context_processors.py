#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 26/08/2020 13:39.

from django.conf import settings  # import the settings file
from .icons import *


def frontend_template_context(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'TOOLTIP_NEW': "Novo",
        'TOOLTIP_EDIT': "Editar",
        'TOOLTIP_DEL': "Deletar",
        'TOOLTIP_BACK': "Voltar",
        'TOOLTIP_PAYMENT_PAY': "Mudar status para pago",
        'TOOLTIP_NEW_SERVICE': "Adicionar novo procedimento",
        'TOOLTIP_NEW_INVOICE': "Adicionar nova fatura",
        'TOOLTIP_SERVICE_CONFIRM': "Confirmar procedimento",
        'TOOLTIP_SERVICE_FINISH': "Mudar status para finalizado",

        'NAME_OF_ENTERPRISE': settings.NAME_OF_ENTERPRISE,
        'VERSION': settings.VERSION,
        'ICON_HOME': ICON_HOME,
        'ICON_LOGOUT': ICON_LOGOUT,
        'ICON_LINK': ICON_LINK,
        'ICON_EYE': ICON_EYE,
        'ICON_ARROW_BACK': ICON_ARROW_BACK,
        'ICON_DELETE': ICON_DELETE,
        'ICON_EDIT': ICON_EDIT,
        'ICON_ADD': ICON_ADD,
        'ICON_CALENDAR': ICON_CALENDAR,
        'ICON_DEVICE': ICON_DEVICE,
        'ICON_PERSON': ICON_PERSON,
        'ICON_NEW_PERSON': ICON_NEW_PERSON,
        'ICON_SETTINGS': ICON_SETTINGS,
        'ICON_TRIANGLE_ALERT': ICON_TRIANGLE_ALERT,
        'ICON_BUG': ICON_BUG,
        'ICON_DASHBOARD': ICON_DASHBOARD,
        'ICON_CHECK': ICON_CHECK,
        'ICON_DOUBLE_CHECK': ICON_DOUBLE_CHECK,
        'ICON_GIFT': ICON_GIFT,
    }
