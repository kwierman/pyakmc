from typer.testing import CliRunner

from pyakmc.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["Camila", "--city", "Berlin"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output
    assert "Let's have a coffee in Berlin" in result.output
