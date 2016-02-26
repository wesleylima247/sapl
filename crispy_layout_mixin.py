from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import HTML, Div, Fieldset, Layout, Submit
from django.utils.translation import ugettext as _


def to_column(name_span):
    fieldname, span = name_span
    return Div(fieldname, css_class='col-md-%d' % span)


def to_row(names_spans):
    return Div(*map(to_column, names_spans), css_class='row-fluid')


def to_fieldsets(fields):
    for field in fields:
        if isinstance(field, list):
            legend, *row_specs = field
            rows = [to_row(name_span_list) for name_span_list in row_specs]
            yield Fieldset(legend, *rows)
        else:
            yield field


def form_actions(more=[], save_label=_('Salvar')):
    return FormActions(
        Submit('salvar', save_label, css_class='pull-right'), *more)


class SaplFormLayout(Layout):

    def __init__(self, *fields):
        buttons = form_actions(more=[
            HTML('<a href="{{ view.cancel_url }}"'
                 ' class="btn btn-inverse">%s</a>' % _('Cancelar'))])
        _fields = list(to_fieldsets(fields)) + [to_row([(buttons, 12)])]
        super(SaplFormLayout, self).__init__(*_fields)