import pytest
import os
import sys
from robot.run import RobotFramework
# from django.core import management
from model_mommy.recipe import Recipe, foreign_key

sys.path.append(os.path.abspath('../..'))

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

    # Persistência
    comissao.make(nome='Teste de Exclusão')
    comissao.make(nome='Teste de Edição')

    # Roda os testes
    RobotFramework().main(['features/tests/comissoes/comissoes_crud.robot'])
