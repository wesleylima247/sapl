from django.apps import apps
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms

# SAPL business apps
#  This is a dependency order: each entry depends only on previous ones
#  The order is important for migration code
appconfs = [apps.get_app_config(n) for n in [
    'parlamentares',
    'comissoes',
    'compilacao',
    'materia',
    'norma',
    'sessao',
    'lexml',
    'protocoloadm', ]]


def register_all_models_in_admin(module_name):
    appname = module_name.split('.')[0]
    app = apps.get_app_config(appname)
    for model in app.get_models():
        class CustomModelAdmin(admin.ModelAdmin):
            list_display = [f.name for f in model._meta.fields
                            if f.name != 'id']

        if not admin.site.is_registered(model):
            admin.site.register(model, CustomModelAdmin)


def xstr(s):
    return '' if s is None else str(s)


def create_barcode(value):
    '''
        creates a base64 encoded barcode PNG image
    '''
    from base64 import b64encode
    from reportlab.graphics.barcode import createBarcodeDrawing

    barcode = createBarcodeDrawing('Code128',
                                   value=value,
                                   barWidth=170,
                                   height=50,
                                   fontSize=2,
                                   humanReadable=True)
    data = b64encode(barcode.asString('png'))
    return data.decode('utf-8')


def make_choices(*choice_pairs):
    assert len(choice_pairs) % 2 == 0
    ipairs = iter(choice_pairs)
    choices = list(zip(ipairs, ipairs))
    yield choices
    for key, value in choices:
        yield key

YES_NO_CHOICES = [(True, _('Sim')), (False, _('Não'))]


# Validador de PDFS, DOCX, ODT e ZIP as
# Classes UploadedFileInMemoryError e DocField


class UploadedFileInMemoryError(Exception):
    pass


class DocField(forms.FileField):
    default_error_messages = {
        'invalid': _(u"Envie algum arquivo com o formato especificado."),
        'missing': _(u"Nenhum arquivo enviado"),
        'empty': _(u"O arquivo enviado está vazio"),
        'not_doc': _(u"Envie um documento válido. O documento está corrompido\
                       ou não é do formato especificado."),
    }

    def clean(self, data, initial=None):
        super(DocField, self).clean(initial or data)

        # before save check if the writing sample is valid
        import os
        import re
        from django.forms.util import ValidationError

        match = r'PDF document|Microsoft Office Document|\
                  Zip archive data|Document'

        if hasattr(data, 'temporary_file_path'):
            file = data.temporary_file_path()
        else:
            # throw an error because uploaded file in memory
            raise UploadedFileInMemoryError('O arquivo inserido não\
                está salvo no disco rígido.')

        out = os.popen('file %s' % file)
        ck = re.search(match, out.read())
        if ck is None:
            raise ValidationError(self.error_messages['not_doc'])
        #  check further for docx file as it's zip file
        if ck.group(0)[0] == 'Z':
            import zipfile
            docx = 'word/document.xml'
            if not zipfile.is_zipfile(file):
                raise ValidationError(self.error_messages['not_doc'])

            zf = zipfile.ZipFile(file)
            if docx not in zf.namelist():
                raise ValidationError(self.error_messages['not_doc'])
        return data
