from opalina.cli import CLI


def test_auto_config():
    cli = CLI._auto()
    assert isinstance(cli, CLI)
    assert isinstance(cli.version, str)
