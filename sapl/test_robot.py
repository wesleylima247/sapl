import pytest
from robot.run import RobotFramework

pytestmark = pytest.mark.django_db


def test_robot(live_server):
    RobotFramework().main(['features'])
