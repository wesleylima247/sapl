from django.db import models
from django.template import defaultfilters
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices

from materia.models import MateriaLegislativa
from sapl.utils import RANGE_ANOS, YES_NO_CHOICES


class AssuntoNorma(models.Model):
    assunto = models.CharField(max_length=50, verbose_name=_('Assunto'))
    descricao = models.CharField(
        max_length=250, blank=True, verbose_name=_('Descrição'))

    class Meta:
        verbose_name = _('Assunto de Norma')
        verbose_name_plural = _('Assuntos de Norma')

    def __str__(self):
        return self.assunto


class TipoNormaJuridica(models.Model):
    # TODO transform into Domain Model and use an FK for the field
    EQUIVALENTE_LEXML_CHOICES = ((name, name) for name in
                                 ('constituicao',
                                  'ementa.constitucional',
                                  'lei.complementar',
                                  'lei.delegada',
                                  'lei',
                                  'decreto.lei',
                                  'medida.provisoria',
                                  'decreto',
                                  'lei.organica',
                                  'emenda.lei.organica',
                                  'decreto.legislativo',
                                  'resolucao',
                                  'regimento.interno',
                                  ))
    equivalente_lexml = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_('Equivalente LexML'),
        choices=EQUIVALENTE_LEXML_CHOICES)
    sigla = models.CharField(max_length=3, verbose_name=_('Sigla'))
    descricao = models.CharField(max_length=50, verbose_name=_('Descrição'))

    class Meta:
        verbose_name = _('Tipo de Norma Jurídica')
        verbose_name_plural = _('Tipos de Norma Jurídica')

    def __str__(self):
        return self.descricao


def get_norma_media_path(instance, subpath, filename):
    return './norma/%s/%s/%s' % (instance, subpath, filename)


def texto_upload_path(instance, filename):
    return get_norma_media_path(instance, instance.ano, filename)


class NormaJuridica(models.Model):
    ESFERA_FEDERACAO_CHOICES = Choices(
        ('E', 'estadual', _('Estadual')),
        ('F', 'federal', _('Federal')),
        ('M', 'municipal', _('Municipal')),
    )
    texto_integral = models.FileField(
        blank=True,
        null=True,
        upload_to=texto_upload_path,
        verbose_name=_('Texto Integral'))
    tipo = models.ForeignKey(
        TipoNormaJuridica, verbose_name=_('Tipo da Norma Juridica'))
    materia = models.ForeignKey(MateriaLegislativa, blank=True, null=True)
    numero = models.PositiveIntegerField(verbose_name=_('Número'))
    ano = models.PositiveSmallIntegerField(verbose_name=_('Ano'),
                                           choices=RANGE_ANOS)
    esfera_federacao = models.CharField(
        max_length=1,
        verbose_name=_('Esfera Federação'),
        choices=ESFERA_FEDERACAO_CHOICES)
    data = models.DateField(verbose_name=_('Data'))
    data_publicacao = models.DateField(
        blank=True, null=True, verbose_name=_('Data Publicação'))
    veiculo_publicacao = models.CharField(
        max_length=30,
        blank=True,
        verbose_name=_('Veículo Publicação'))
    pagina_inicio_publicacao = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('Pg. Início'))
    pagina_fim_publicacao = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=_('Pg. Fim'))
    ementa = models.TextField(verbose_name=_('Ementa'))
    indexacao = models.TextField(
        blank=True, verbose_name=_('Indexação'))
    observacao = models.TextField(
        blank=True, verbose_name=_('Observação'))
    complemento = models.NullBooleanField(
        blank=True, verbose_name=_('Complementar ?'),
        choices=YES_NO_CHOICES)
    # XXX was a CharField (attention on migrate)
    assuntos = models.ManyToManyField(
        AssuntoNorma,
        through='AssuntoNormaRelationship')
    data_vigencia = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name = _('Norma Jurídica')
        verbose_name_plural = _('Normas Jurídicas')
        ordering = ['-data', '-numero']

    def __str__(self):
        return _('%(tipo)s nº %(numero)s de %(data)s') % {
            'tipo': self.tipo,
            'numero': self.numero,
            'data': defaultfilters.date(self.data, "d \d\e F \d\e Y")}


class AssuntoNormaRelationship(models.Model):
    assunto = models.ForeignKey(AssuntoNorma)
    norma = models.ForeignKey(NormaJuridica)

    class Meta:
        unique_together = (
            ('assunto', 'norma'),
        )


class LegislacaoCitada(models.Model):
    materia = models.ForeignKey(MateriaLegislativa)
    norma = models.ForeignKey(NormaJuridica)
    disposicoes = models.CharField(
        max_length=15, blank=True, verbose_name=_('Disposição'))
    parte = models.CharField(
        max_length=8, blank=True, verbose_name=_('Parte'))
    livro = models.CharField(
        max_length=7, blank=True, verbose_name=_('Livro'))
    titulo = models.CharField(
        max_length=7, blank=True, verbose_name=_('Título'))
    capitulo = models.CharField(
        max_length=7, blank=True, verbose_name=_('Capítulo'))
    secao = models.CharField(
        max_length=7, blank=True, verbose_name=_('Seção'))
    subsecao = models.CharField(
        max_length=7, blank=True, verbose_name=_('Subseção'))
    artigo = models.CharField(
        max_length=4, blank=True, verbose_name=_('Artigo'))
    paragrafo = models.CharField(
        max_length=3, blank=True, verbose_name=_('Parágrafo'))
    inciso = models.CharField(
        max_length=10, blank=True, verbose_name=_('Inciso'))
    alinea = models.CharField(
        max_length=3, blank=True, verbose_name=_('Alínea'))
    item = models.CharField(
        max_length=3, blank=True, verbose_name=_('Item'))

    class Meta:
        verbose_name = _('Matéria Legislativa')
        verbose_name_plural = _('Matérias Legislativas')


class VinculoNormaJuridica(models.Model):
    TIPO_VINCULO_CHOICES = (
        ('A', _('Altera a norma')),
        ('R', _('Revoga integralmente a norma')),
        ('P', _('Revoga parcialmente a norma')),
        ('T', _('Revoga integralmente por consolidação')),
        ('C', _('Norma correlata')),
        ('S', _('Ressalva a norma')),
        ('E', _('Reedita a norma')),
        ('I', _('Reedita a norma com alteração')),
        ('G', _('Regulamenta a norma')),
        ('K', _('Suspende parcialmente a norma')),
        ('L', _('Suspende integralmente a norma')),
        ('N', _('Julgada integralmente inconstitucional')),
        ('O', _('Julgada parcialmente inconstitucional')),
    )

    # TODO M2M ???
    norma_referente = models.ForeignKey(
        NormaJuridica, related_name='norma_referente_set')
    norma_referida = models.ForeignKey(
        NormaJuridica, related_name='norma_referida_set')
    tipo_vinculo = models.CharField(
        max_length=1, blank=True, choices=TIPO_VINCULO_CHOICES)

    class Meta:
        verbose_name = _('Vínculo entre Normas Jurídicas')
        verbose_name_plural = _('Vínculos entre Normas Jurídicas')

    def __str__(self):
        return _('Referente: %(referente)s \n'
                 'Referida: %(referida)s \nVínculo: %(vinculo)s') % {
            'referente': self.norma_referente,
            'referida': self.norma_referida,
            'vinculo': self.tipo_vinculo}
