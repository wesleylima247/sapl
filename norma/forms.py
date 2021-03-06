from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout
from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms import ModelForm

import crispy_layout_mixin
from crispy_layout_mixin import form_actions
from materia.models import MateriaLegislativa, TipoMateriaLegislativa
from sapl.settings import MAX_DOC_UPLOAD_SIZE
from sapl.utils import RANGE_ANOS

from .models import NormaJuridica


def get_esferas():
    return [('E', 'Estadual'),
            ('F', 'Federal'),
            ('M', 'Municipal')]


class NormaJuridicaPesquisaForm(ModelForm):

    periodo_inicial = forms.DateField(label=u'Período Inicial',
                                      input_formats=['%d/%m/%Y'],
                                      required=False,
                                      widget=forms.DateInput(
                                        format='%d/%m/%Y',
                                        attrs={'class': 'dateinput'}))

    periodo_final = forms.DateField(label=u'Período Final',
                                    input_formats=['%d/%m/%Y'],
                                    required=False,
                                    widget=forms.DateInput(
                                        format='%d/%m/%Y',
                                        attrs={'class': 'dateinput'}))

    publicacao_inicial = forms.DateField(label=u'Publicação Inicial',
                                         input_formats=['%d/%m/%Y'],
                                         required=False,
                                         widget=forms.DateInput(
                                            format='%d/%m/%Y',
                                            attrs={'class': 'dateinput'}))

    publicacao_final = forms.DateField(label=u'Publicação Final',
                                       input_formats=['%d/%m/%Y'],
                                       required=False,
                                       widget=forms.DateInput(
                                            format='%d/%m/%Y',
                                            attrs={'class': 'dateinput'}))

    ano = forms.ModelChoiceField(
        label='Ano',
        required=False,
        queryset=NormaJuridica.objects.order_by('ano').values_list(
            'ano', flat=True).distinct(),
        empty_label='Selecione'
    )

    class Meta:
        model = NormaJuridica
        fields = ['tipo',
                  'numero',
                  'ano',
                  'periodo_inicial',
                  'periodo_final',
                  'publicacao_inicial',
                  'publicacao_final']

    def __init__(self, *args, **kwargs):

        row1 = crispy_layout_mixin.to_row(
            [('tipo', 12)])

        row2 = crispy_layout_mixin.to_row(
            [('numero', 6), ('ano', 6)])

        row3 = crispy_layout_mixin.to_row(
            [('periodo_inicial', 6), ('periodo_final', 6)])

        row4 = crispy_layout_mixin.to_row(
            [('publicacao_inicial', 6), ('publicacao_final', 6)])

        self.helper = FormHelper()
        self.helper.layout = Layout(
             Fieldset('Pesquisa Norma Juridica',
                      row1, row2, row3, row4),
             form_actions(save_label='Pesquisar')
        )
        super(NormaJuridicaPesquisaForm, self).__init__(*args, **kwargs)


class NormaJuridicaForm(ModelForm):

    # Campos de MateriaLegislativa
    tipo_materia = forms.ModelChoiceField(
        label='Matéria',
        required=False,
        queryset=TipoMateriaLegislativa.objects.all(),
        empty_label='Selecione'
    )
    numero_materia = forms.CharField(
        label='Número Matéria',
        required=False
    )
    ano_materia = forms.ChoiceField(
        label='Ano Matéria',
        required=False,
        choices=RANGE_ANOS,
    )

    class Meta:
        model = NormaJuridica
        fields = ['tipo',
                  'numero',
                  'ano',
                  'data',
                  'esfera_federacao',
                  'complemento',
                  'tipo_materia',
                  'numero_materia',
                  'ano_materia',
                  'data_publicacao',
                  'veiculo_publicacao',
                  'pagina_inicio_publicacao',
                  'pagina_fim_publicacao',
                  'ementa',
                  'indexacao',
                  'observacao',
                  'texto_integral']

    def clean(self):
        cleaned_data = self.cleaned_data

        if (cleaned_data['tipo_materia'] and
            cleaned_data['numero_materia'] and
                cleaned_data['ano_materia']):

            try:
                materia = MateriaLegislativa.objects.get(
                    tipo_id=cleaned_data['tipo_materia'],
                    numero=cleaned_data['numero_materia'],
                    ano=cleaned_data['ano_materia'])
            except ObjectDoesNotExist:
                raise forms.ValidationError("Matéria escolhida não existe!")
            else:
                cleaned_data['materia'] = materia

        else:
            cleaned_data['materia'] = None
        return cleaned_data

    def clean_texto_integral(self):
        texto_integral = self.cleaned_data.get('texto_integral', False)
        if texto_integral:
            if texto_integral.size > MAX_DOC_UPLOAD_SIZE:
                raise ValidationError("Arquivo muito grande. ( > 5mb )")
            return texto_integral

    def save(self, commit=False):
        norma = super(NormaJuridicaForm, self).save(commit)
        norma.timestamp = datetime.now()
        norma.materia = self.cleaned_data['materia']
        norma.save()
        return norma
