import pytest
import os
import sys
from datetime import date
from robot.run import RobotFramework
# from django.core import management
from model_mommy.recipe import Recipe, foreign_key

sys.path.append(os.path.abspath('..'))

pytestmark = pytest.mark.django_db


def test_robot(live_server):
    # Flush do banco. Útil pra zerar auto-incremento.
    # management.call_command('flush')

    # Recipes model mommy
    tipo_da_comissao = Recipe(
        'comissoes.TipoComissao',
        nome='Tipo da Comissão',
    )

    comissao = Recipe(
        'comissoes.Comissao',
        nome='',
        tipo=foreign_key(tipo_da_comissao),
    )

    composicao = Recipe(
        'comissoes.Composicao',
        comissao=foreign_key(comissao),
    )

    parlamentar = Recipe(
        'parlamentares.Parlamentar',
        nome_completo='Nome Completo',
        nome_parlamentar='Nome Parlamentar',
        ativo=True,
    )

    partido = Recipe(
        'parlamentares.Partido',
        sigla='NdP',
        nome='Nome do Partido',
        data_criacao=date.today,
        data_extincao=None,
    )

    filiacao = Recipe(
        'parlamentares.Filiacao',
        data=date.today,
        parlamentar=foreign_key(parlamentar),
        partido=foreign_key(partido),
        data_desfiliacao=None,
    )

    cargo_comissao = Recipe(
        'comissoes.CargoComissao',
        nome='Cargo Comissão',
        unico=True,
    )

    participacao = Recipe(
        'comissoes.Participacao',
        composicao=foreign_key(composicao),
        parlamentar=foreign_key(parlamentar),
        cargo=foreign_key(cargo_comissao),
    )

    # Persistência
    comissao.make(nome='Teste de Exclusão CRUD')
    comissao.make(nome='Teste de Edição CRUD')
    composicao.make(comissao__nome='Teste de Inclusão Parlamentar')
    filiacao.make()
    filiacao_edicao = filiacao.make(
        parlamentar__nome_completo='Edição Nome Completo',
        parlamentar__nome_parlamentar='Edição Nome Parlamentar',
    )
    cargo_comissao.make()
    participacao.make(
        parlamentar=filiacao_edicao.parlamentar,
        composicao__comissao__nome='Teste de Edição Parlamentar',
    )

    # Roda os testes
    RobotFramework().main(['features'])
