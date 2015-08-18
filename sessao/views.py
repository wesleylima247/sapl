from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Field, Fieldset, Layout, Submit
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from extra_views import FormSetView
from parlamentares.models import Parlamentar
from sapl.crud import build_crud

from .models import (ExpedienteMateria, ExpedienteSessao, OrdemDia,
                     RegistroVotacao, SessaoPlenaria, SessaoPlenariaPresenca,
                     TipoExpediente, TipoResultadoVotacao, TipoSessaoPlenaria)

tipo_sessao_crud = build_crud(
    TipoSessaoPlenaria, 'tipo_sessao_plenaria', [

        [_('Tipo de Sessão Plenária'),
         [('nome', 6), ('quorum_minimo', 6)]],
    ])

sessao_crud = build_crud(
    SessaoPlenaria, '', [

        [_('Dados Básicos'),
         [('numero', 1),
            ('tipo', 3),
            ('legislatura', 4),
            ('sessao_legislativa', 4)],
            [('data_inicio', 5), ('hora_inicio', 5), ('iniciada', 2)],
            [('data_fim', 5), ('hora_fim', 5), ('finalizada', 2)],
            [('upload_pauta', 6), ('upload_ata', 6)],
            [('url_audio', 6), ('url_video', 6)]],
    ])

expediente_materia_crud = build_crud(
    ExpedienteMateria, '', [

        [_('Cadastro de Matérias do Expediente'),
         [('data_ordem', 4), ('tip_sessao_FIXME', 4), ('numero_ordem', 4)],
            [('tip_id_basica_FIXME', 4),
             ('num_ident_basica_FIXME', 4),
             ('ano_ident_basica_FIXME', 4)],
            [('tipo_votacao', 12)],
            [('observacao', 12)]],
    ])

ordem_dia_crud = build_crud(
    OrdemDia, '', [

        [_('Cadastro de Matérias da Ordem do Dia'),
         [('data_ordem', 4), ('tip_sessao_FIXME', 4), ('numero_ordem', 4)],
            [('tip_id_basica_FIXME', 4),
             ('num_ident_basica_FIXME', 4),
             ('ano_ident_basica_FIXME', 4)],
            [('tipo_votacao', 12)],
            [('observacao', 12)]],
    ])

tipo_resultado_votacao_crud = build_crud(
    TipoResultadoVotacao, 'tipo_resultado_votacao', [

        [_('Tipo de Resultado da Votação'),
         [('nome', 12)]],
    ])

tipo_expediente_crud = build_crud(
    TipoExpediente, 'tipo_expediente', [

        [_('Tipo de Expediente'),
         [('nome', 12)]],
    ])

registro_votacao_crud = build_crud(
    RegistroVotacao, '', [

        [_('Votação Simbólica'),
         [('numero_votos_sim', 3),
            ('numero_votos_nao', 3),
            ('numero_abstencoes', 3),
            ('nao_votou_FIXME', 3)],
            [('votacao_branco_FIXME', 6),
             ('ind_votacao_presidente_FIXME', 6)],
            [('tipo_resultado_votacao', 12)],
            [('observacao', 12)]],
    ])


class ExpedienteForm(ModelForm):
    # tipo = forms.CharField()

    class Meta:
        model = ExpedienteSessao
        fields = ['tipo', 'conteudo']

    def __init__(self, *args, **kwargs):
        super(ExpedienteForm, self).__init__(*args, **kwargs)
        # for i, values in enumerate(TipoExpediente.objects.all()):
        #    self.fields['tipo'] = forms.CharField(required=False)


class ExpedienteView(FormSetView, sessao_crud.CrudDetailView):
    form_class = ExpedienteForm
    template_name = 'sessao/expediente.html'

    data = {'form-TOTAL_FORMS': '6',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '', }

    ExpedienteFormSet = modelformset_factory(ExpedienteSessao,
                                             form=ExpedienteForm,
                                             fields=('tipo', 'conteudo'))
    formset = ExpedienteFormSet(data)

    def formset_valid(self, formset):
        self.object = self.get_object()
        expediente = ExpedienteSessao.objects.filter(
            sessao_plenaria_id=self.object.id)

        for form in formset.cleaned_data:
            expediente.filter(tipo=form['tipo']).update(
                conteudo=form['conteudo'])

        return super(ExpedienteView, self).formset_valid(formset)
