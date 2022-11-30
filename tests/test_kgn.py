import spacy
from os import system

from kgn.cli import cli

system("python -m spacy download en_core_web_sm")

from click.testing import CliRunner

def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")
