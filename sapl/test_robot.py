import pytest
import os
import sys
from robot.run import RobotFramework
# from django.core import management
from model_mommy import mommy
from comissoes.models import TipoComissao
sys.path.append(os.path.abspath('..'))

pytestmark = pytest.mark.django_db


def test_robot(live_server):
    # Isso pode ser útil. Este comando dá flush no banco.
    # management.call_command('flush')
    mommy.make(TipoComissao, nome='Tipo da comissão')
    RobotFramework().main(['features'])
