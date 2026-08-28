"""Tests for the installed command's Python entry point."""

import json

import pytest

from numerology.cli import main


def test_cli_writes_a_json_reading(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["Ada", "Lovelace", "1815-12-10"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["destiny"] == 9
    assert output["life_path_interpretation"]["title"] == "The Path of Independence"
