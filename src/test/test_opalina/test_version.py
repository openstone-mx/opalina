from opalina.version import version


def test_semver_specification():
    components = version.split(".")
    assert len(components) == 3
    for component in components:
        assert component.isdigit()
