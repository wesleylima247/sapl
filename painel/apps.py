from django import apps
from django.utils.translation import ugettext_lazy as _


class AppConfig(apps.AppConfig):
    name = 'painel'
    verbose_name = _('Painel Eletrônico')
