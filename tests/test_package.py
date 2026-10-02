from importlib.metadata import version

import vnacourse


def test_version_matches_metadata():
    assert vnacourse.__version__ == version("vnacourse")
