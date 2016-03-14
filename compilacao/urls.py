from django.conf.urls import include, url

from compilacao import views
from compilacao.views import (tipo_nota_crud, tipo_publicacao_crud,
                              tipo_vide_crud, veiculo_publicacao_crud)

urlpatterns_compilacao = [
    url(r'^$', views.TaListView.as_view(), name='ta_list'),
    url(r'^create$', views.TaCreateView.as_view(), name='ta_create'),
    url(r'^(?P<pk>\d+)$', views.TaDetailView.as_view(), name='ta_detail'),
    url(r'^(?P<pk>\d+)/edit$',
        views.TaUpdateView.as_view(), name='ta_edit'),
    url(r'^(?P<pk>\d+)/delete$',
        views.TaDeleteView.as_view(), name='ta_delete'),


    url(r'^(?P<ta_id>\d+)/text$',
        views.TextView.as_view(), name='ta_text'),

    url(r'^(?P<ta_id>\d+)/text/vigencia/(?P<sign>.+)/$',
        views.TextView.as_view(), name='ta_vigencia'),

    url(r'^(?P<ta_id>\d+)/text/edit',
        views.TextEditView.as_view(), name='ta_text_edit'),

    url(r'^(?P<ta_id>\d+)/text/(?P<dispositivo_id>\d+)/$',
        views.DispositivoView.as_view(), name='dispositivo'),

    url(r'^(?P<ta_id>\d+)/text/(?P<dispositivo_id>\d+)/refresh',
        views.DispositivoEditView.as_view(), name='dispositivo_edit'),

    url(r'^(?P<ta_id>\d+)/text/(?P<dispositivo_id>\d+)/actions',
        views.ActionsEditView.as_view(), name='dispositivo_actions'),



    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/nota/create$',
        views.NotasCreateView.as_view(), name='nota_create'),

    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/nota/(?P<pk>\d+)/edit$',
        views.NotasEditView.as_view(), name='nota_edit'),

    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/nota/(?P<pk>\d+)/delete$',
        views.NotasDeleteView.as_view(), name='nota_delete'),

    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/vide/create$',
        views.VideCreateView.as_view(), name='vide_create'),

    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/vide/(?P<pk>\d+)/edit$',
        views.VideEditView.as_view(), name='vide_edit'),

    url(r'^(?P<ta_id>\d+)/text/'
        '(?P<dispositivo_id>\d+)/vide/(?P<pk>\d+)/delete$',
        views.VideDeleteView.as_view(), name='vide_delete'),

    url(r'^(?P<ta_id>\d+)/text/search$',
        views.DispositivoSearchFragmentFormView.as_view(),
        name='search_dispositivo'),


    url(r'^(?P<ta_id>\d+)/publicacao$',
        views.PublicacaoListView.as_view(), name='ta_pub_list'),
    url(r'^(?P<ta_id>\d+)/publicacao/create$',
        views.PublicacaoCreateView.as_view(), name='ta_pub_create'),
    url(r'^(?P<ta_id>\d+)/publicacao/(?P<pk>\d+)$',
        views.PublicacaoDetailView.as_view(), name='ta_pub_detail'),
    url(r'^(?P<ta_id>\d+)/publicacao/(?P<pk>\d+)/edit$',
        views.PublicacaoUpdateView.as_view(), name='ta_pub_edit'),
    url(r'^(?P<ta_id>\d+)/publicacao/(?P<pk>\d+)/delete$',
        views.PublicacaoDeleteView.as_view(), name='ta_pub_delete'),


    url(r'^config/tipo-textoarticulado$',
        views.TipoTaListView.as_view(), name='tipo_ta_list'),
    url(r'^config/tipo-textoarticulado/create$',
        views.TipoTaCreateView.as_view(), name='tipo_ta_create'),
    url(r'^config/tipo-textoarticulado/(?P<pk>\d+)$',
        views.TipoTaDetailView.as_view(), name='tipo_ta_detail'),
    url(r'^config/tipo-textoarticulado/(?P<pk>\d+)/edit$',
        views.TipoTaUpdateView.as_view(), name='tipo_ta_edit'),
    url(r'^config/tipo-textoarticulado/(?P<pk>\d+)/delete$',
        views.TipoTaDeleteView.as_view(), name='tipo_ta_delete'),


]

urlpatterns = [
    url(r'^ta/', include(urlpatterns_compilacao, 'compilacao', 'compilacao')),

    url(r'^ta/config/tipo-nota/',
        include(tipo_nota_crud.urls)),
    url(r'^ta/config/tipo-vide/',
        include(tipo_vide_crud.urls)),
    url(r'^ta/config/tipo-publicacao/',
        include(tipo_publicacao_crud.urls)),
    url(r'^ta/config/veiculo-publicacao/',
        include(veiculo_publicacao_crud.urls)),

]
