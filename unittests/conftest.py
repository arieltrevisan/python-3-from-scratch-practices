import pytest


@pytest.fixture(scope="module")
def setup_only_once():
    print("[SETUP ONLY ONCE]")


@pytest.fixture()
def setup_each_method():
    print("[SETUP EACH]")
