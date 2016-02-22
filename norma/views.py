from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.http import HttpResponseRedirect
from compilacao.views import IntegracaoTaView
from crud import build_crud
from django.views.generic import CreateView
from .models import (AssuntoNorma, LegislacaoCitada, NormaJuridica,
                     TipoNormaJuridica)
from .forms import NormaJuridicaForm
from django.core.urlresolvers import reverse
from materia.models import MateriaLegislativa
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

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

# norma_crud = build_crud(

#     NormaJuridica, '', [

#         [_('Identificação Básica'),
#          [('tipo', 4), ('numero', 4), ('ano', 4)],
#             [('data', 4), ('esfera_federacao', 4), ('complemento', 4)],
#             [('materi', 4),
#              ('numero', 4),
#              ('ano', 4)],
#             [('data_publicacao', 3),
#              ('veiculo_publicacao', 3),
#              ('pagina_inicio_publicacao', 3),
#              ('pagina_fim_publicacao', 3)],
#             [('texto_integral', 12)],
#             [('ementa', 12)],
#             [('indexacao', 12)],
#             [('observacao', 12)]],
#     ])

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


# class NormaIncluirView(FormMixin, GenericView):
#     template_name = "norma/normajuridica_incluir.html"

#     def get_success_url(self):
#         return '/norma/'

#     def get(self, request, *args, **kwargs):
#         form = NormaJuridicaForm()
#         return self.render_to_response({'form': form})

#     def post(self, request, *args, **kwargs):
#         form = NormaJuridicaForm(request.POST or None)
#         if form.is_valid():
#             norma = form.save(commit=False)

#             if form.cleaned_data['tipo_materia']:
#                 tipo = TipoMateriaLegislativa.objects.get(
#                     id=form.cleaned_data['tipo_materia'])
#                 try:
#                     materia = MateriaLegislativa.objects.get(
#                         tipo=tipo,
#                         numero=form.cleaned_data['numero'],
#                         ano=form.cleaned_data['ano'])
#                 except ObjectDoesNotExist:
#                     return self.render_to_response(
#                         {'form': form,
#                          'error': 'Matéria adicionada não existe!'})
#                 else:
#                     norma.materia = materia

#             if form.cleaned_data['indexacao']:
#                 norma.indexacao = sub(
#                     '&nbsp;', ' ', strip_tags(form.cleaned_data['indexacao']))

#             if form.cleaned_data['observacao']:
#                 norma.observacao = sub(
#                     '&nbsp;', ' ', strip_tags(form.cleaned_data['observacao']))

#             if 'texto_integral' in request.FILES:
#                 norma.texto_integral = request.FILES['texto_integral']

#             norma.ementa = sub(
#                 '&nbsp;', ' ', strip_tags(form.cleaned_data['ementa']))
#             norma.timestamp = datetime.now()
#             norma.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

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


class NormaTaView(IntegracaoTaView):
    model = NormaJuridica
    model_type_foreignkey = TipoNormaJuridica
