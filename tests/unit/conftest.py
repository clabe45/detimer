import pytest

from detimer.app import App
from detimer.root import Root, SpecialFileMode


@pytest.fixture
def click(mocker) -> App:
    """Mock the click module"""

    mocker.patch("detimer.cli.click")
    mocker.patch("detimer.commands.click")


@pytest.fixture
def app(mocker) -> App:
    """Mock the click app"""

    app = mocker.Mock(spec=App)
    root1 = mocker.Mock(spec=Root)
    root1.name = "root1"
    root1.source = "source1"
    root1.special_files = SpecialFileMode.DETECT
    root1.destination = "destination1"

    root2 = mocker.Mock(spec=Root)
    root2.name = "root2"
    root2.source = "source2"
    root1.special_files = SpecialFileMode.DETECT
    root2.destination = "destination2"

    app.roots = {
        root1.name: root1,
        root2.name: root2,
    }

    return app
