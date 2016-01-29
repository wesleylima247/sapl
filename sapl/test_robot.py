import pytest
from subprocess import call
from model_mommy import mommy
from .utils import appconfs

pytestmark = pytest.mark.django_db


def test_robot(live_server):
    for app in appconfs:
        for model in app.get_models():
            mommy.make(model)

    call(['pybot', 'features/'])
