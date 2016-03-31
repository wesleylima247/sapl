from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BaseAppConfig(AppConfig):
    name = 'base'
    verbose_name = _('Dados Básicos')


class ProblemaMigracao(AppConfig):
    name = 'problemamigracao'
    verbose_name = _('Problemas da Migração')
