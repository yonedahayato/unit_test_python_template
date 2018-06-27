import pytest
import time
from io import StringIO

@pytest.fixture(scope="module", autouse=True)
def setUp_tearDown():
    # set up processing
    setUp_object = StringIO("12345")
    time.sleep(1)
    print ("created!")

    yield setUp_object

    # taer dwon processing
    time.sleep(1)
    setUp_object.close()
    print("closed!")

def test_1():
    a = 1
    b = 2
    assert a == b

def test_2():
    a = 1
    b = 2
    assert a != b

def test_3(setUp_tearDown):
    assert setUp_tearDown.getvalue() == "2345"

def test_4(setUp_tearDown):
    assert setUp_tearDown.getvalue() == "2345"

parameter_key = "x, y"
parameter_value = [
    ("aaa", "bbb"),
    ("aaa", "aaa"),
    ("bbb", "bbb")
]

@pytest.mark.parametrize(parameter_key, parameter_value)
def test_5(x, y):
    assert x == y

@pytest.mark.parametrize(parameter_key, parameter_value)
@pytest.mark.small
def test_6(x, y):
    time.sleep(0.1)
    assert x == y

@pytest.mark.parametrize(parameter_key, parameter_value)
@pytest.mark.small
def test_7(x, y):
    time.sleep(0.1)
    assert x == y

@pytest.mark.parametrize(parameter_key, parameter_value)
@pytest.mark.large
def test_8(x, y):
    time.sleep(5)
    assert x == y

# memo
# pytest --durations=0
# pytest -m small
# pytest -v
# pytest -n 2
