import logging

from tests import loader


def test_no_schemes(tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    loader.load(
        tmpdir,
        {
            "invalid": {
                "open_api": {
                    "definition": {
                        "swagger": "2.0",
                        "paths": {
                            "/test": {
                                "get": {
                                    "responses": {
                                        "200": {
                                            "description": "return value",
                                            "schema": {"type": "string"},
                                        }
                                    },
                                }
                            }
                        },
                    },
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert caplog.messages == [
        '"invalid" will not be available: Invalid Definition: At least one scheme must be provided.'
    ]


def test_no_host(tmpdir, caplog):
    caplog.set_level(logging.ERROR, logger="pyxelrest")
    loader.load(
        tmpdir,
        {
            "invalid": {
                "open_api": {
                    "definition": {
                        "swagger": "2.0",
                        "schemes": ["https"],
                        "paths": {
                            "/test": {
                                "get": {
                                    "responses": {
                                        "200": {
                                            "description": "return value",
                                            "schema": {"type": "string"},
                                        }
                                    },
                                }
                            }
                        },
                    },
                },
                "formulas": {"dynamic_array": {"lock_excel": True}},
            }
        },
    )
    assert caplog.messages == [
        '"invalid" will not be available: Invalid Definition: host must be provided.'
    ]
