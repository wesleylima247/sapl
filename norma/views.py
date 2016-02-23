from datetime import datetime

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView

from compilacao.views import IntegracaoTaView
from crud import build_crud
from materia.models import MateriaLegislativa

from .forms import NormaJuridicaForm
from .models import (AssuntoNorma, LegislacaoCitada, NormaJuridica,
                     TipoNormaJuridica)

assunto_norma_crud = build_crud(
    AssuntoNorma, 'assunto_norma_juridica', [

        [_('Assunto Norma Jurídica'),
         [('assunto', 6), ('descricao', 6)]],
    ])

tipo_norma_crud = build_crud(
    TipoNormaJuridica, 'tipo_norma_juridica', [

        [_('Tipo Norma Jurídica'),
         [('descricao', 4),
            ('sigla', 4),
            ('equivalente_lexml', 4)]],
    ])


norma_temporario_crud = build_crud(
    NormaJuridica, 'normajuridica', [

        [_('Identificação Básica'),
         [('tipo', 4), ('numero', 4), ('ano', 4)],
            [('data', 4), ('esfera_federacao', 4), ('complemento', 4)],
            [('materia', 12)],
            [('data_publicacao', 3),
             ('veiculo_publicacao', 3),
             ('pagina_inicio_publicacao', 3),
             ('pagina_fim_publicacao', 3)],
            [('texto_integral', 12)],
            [('ementa', 12)],
            [('indexacao', 12)],
            [('observacao', 12)]],
    ])


legislacao_citada_crud = build_crud(
    LegislacaoCitada, '', [

        [_('Legislação Citada'),
         [('tip_norma_FIXME', 4),
            ('num_norma_FIXME', 4),
            ('ano_norma_FIXME', 4)],
            [('disposicoes', 3), ('parte', 3), ('livro', 3), ('titulo', 3)],
            [('capitulo', 3), ('secao', 3), ('subsecao', 3), ('artigo', 3)],
            [('paragrafo', 3), ('inciso', 3), ('alinea', 3), ('item', 3)]],
    ])


class NormaIncluirView(CreateView):
    template_name = "norma/normajuridica_incluir.html"
    form_class = NormaJuridicaForm

    def get_success_url(self):
        return reverse('normajuridica:list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            norma = form.save(commit=False)

            if form.cleaned_data['tipo_materia']:
                try:
                    materia = MateriaLegislativa.objects.get(
                        tipo_id=form.cleaned_data['tipo_materia'],
                        numero=form.cleaned_data['numero_materia'],
                        ano=form.cleaned_data['ano_materia'])
                except ObjectDoesNotExist:
                    msg = 'Matéria adicionada não existe!'
                    messages.add_message(request, messages.INFO, msg)
                    return self.render_to_response({'form': form})
                else:
                    norma.timestamp = datetime.now()
                    norma.materia = materia
                    norma.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response({'form': form})


class NormaEditView(CreateView):
    template_name = "norma/normajuridica_incluir.html"
    form_class = NormaJuridicaForm

    def get(self, request, *args, **kwargs):
        norma = NormaJuridica.objects.get(id=self.kwargs['pk'])
        form = NormaJuridicaForm(instance=norma)
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        norma = NormaJuridica.objects.get(id=self.kwargs['pk'])
        form = NormaJuridicaForm(instance=norma, data=request.POST)

        if form.is_valid():
            if form.data['tipo_materia']:
                try:
                    materia = MateriaLegislativa.objects.get(
                        tipo_id=form.data['tipo_materia'],
                        numero=form.data['numero_materia'],
                        ano=form.data['ano_materia'])
                except ObjectDoesNotExist:
                    msg = 'Matéria adicionada não existe!'
                    messages.add_message(request, messages.INFO, msg)
                    return self.render_to_response({'form': form})
                else:
                    norma.materia = materia
            norma = form.save(commit=False)
            norma.timestamp = datetime.now()
            norma.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response({'form': form})

    def get_success_url(self):
        return reverse('normajuridica:list')


class NormaTaView(IntegracaoTaView):
    model = NormaJuridica
    model_type_foreignkey = TipoNormaJuridica
