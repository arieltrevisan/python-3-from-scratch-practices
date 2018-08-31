import pytest

# setup methods


@pytest.fixture(scope="module")
def setup_only_once(arg1):
    print("[SETUP ONLY ONCE]: args=", arg1)


@pytest.yield_fixture()
def setup_each_method():
    print("[SETUP EACH START]")
    yield
    print("[SETUP EACH END]")


# fixtures uses in classes


@pytest.yield_fixture(scope="class")
def setup_for_class():
    print("[SETUP FOR CLASS START]")
    yield
    print("[SETUP FOR CLASS END]")


@pytest.yield_fixture(scope="class")
def setup_fixture_return(request, arg1):
    if arg1 == "hi":
        value_rtn = 10
    elif arg1 == "bye":
        value_rtn = 20
    else:
        value_rtn = 30

    # assign value_rtn to request to use as
    # return value_rtn where setup_each_method is used.
    if request.cls is not None:
        request.cls.value_rtn = value_rtn

    print("[SETUP FR START]")
    yield value_rtn
    print("[SETUP FR END]")


# command line args:


def pytest_addoption(parser):
    parser.addoption("--arg1", help="Send any value here")


@pytest.fixture(scope="session")
def arg1(request):
    return request.config.getoption("--arg1", default=None)

