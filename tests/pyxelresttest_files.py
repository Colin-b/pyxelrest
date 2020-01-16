import os.path
import tempfile

import pytest
from responses import RequestsMock

from testsutils import serviceshandler, loader


@pytest.fixture
def files_service(responses: RequestsMock):
    from testsutils import files_service

    serviceshandler.start_services((files_service, 8959))
    loader.load("files_services.yml")
    yield 1
    serviceshandler.stop_services()


def test_files_parameter(files_service):
    from pyxelrest import pyxelrestgenerator

    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, "temp_file"), "wb") as temp_file:
            temp_file.write(b"This is the content of the temporary file.")

        assert pyxelrestgenerator.files_post_files(
            mandatory_file="This is the content of the mandatory file.",
            optional_file=temp_file.name,
        ) == [
            ["mandatory_file", "optional_file"],
            [
                "This is the content of the mandatory file.",
                "This is the content of the temporary file.",
            ],
        ]
