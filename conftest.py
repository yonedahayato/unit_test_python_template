import inspect
import logging
import os
import pytest

fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(filename='pytest.log',level=logging.DEBUG, format=fmt)

@pytest.fixture(scope='session', autouse=True)
def scope_session():
    print("setup before session")
    yield
    print("teardown after session")

@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print("    setup before module")
    yield
    print("    teardown after module")

@pytest.fixture(scope='class', autouse=True)
def scope_class():
    print("        setup before class")
    yield
    print("        teardown after class")

def _log():
    def_name = inspect.currentframe().f_back.f_code.co_name
    logging.debug('%s:%s' % (os.getpid(), def_name))

@pytest.fixture(scope='module', autouse=True)
def module():
    _log()

@pytest.fixture(scope='function', autouse=True)
def function():
    _log()
