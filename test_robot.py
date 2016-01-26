import pytest
from subprocess import call

pytestmark = pytest.mark.django_db


def test_bla(live_server):
    call(['pybot', 'features'])
