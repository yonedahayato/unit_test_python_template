import csv
from ctypes import c_wchar_p
import fcntl
from io import StringIO
import logging
from multiprocessing import Array
import os
import pytest
import time

fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(filename='pytest.log',level=logging.DEBUG, format=fmt)

def log(msg):
    logging.debug(msg)

class Operate_File:
    def __init__(self):
        self.filename = "./out.csv"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def write_file(self, msg):
        while True:
            try:
                with open(self.filename, "a+") as f:
                    fcntl.flock(f, fcntl.LOCK_EX)
                    out_str = f.readline()

                    if str(out_str) == "":
                        new_msg = msg
                    else:
                        new_msg = "," + msg

                    f.writelines(new_msg)
                    print(out_str + new_msg)
                    log(msg)
                    break
            except Exception as e:
                log(e)
                continue

class Parameters:
    def __init__(self):
        pass

    def get_params1(self):
        self.parameter_key = "x, y"
        self.parameter_value = [
            ("aaa", "bbb"),
            ("aaa", "aaa"),
            ("bbb", "bbb")
        ]
        self.parameter_len = len(self.parameter_value)

    def get_params2(self, num=5):
        self.parameter_key = "cnt"
        self.parameter_value = range(num)
        self.parameter_len = len(self.parameter_value)

def test_1():
    a = 1
    b = 1
    assert a == b

def test_2():
    a = 1
    b = 2
    assert a != b

p1 = Parameters()
p1.get_params1()

@pytest.mark.parametrize(p1.parameter_key, p1.parameter_value)
def test_parameter1(x, y):
    assert x == y

@pytest.mark.parametrize(p1.parameter_key, p1.parameter_value)
@pytest.mark.small
def test_mark1(x, y):
    time.sleep(0.1)
    assert x == y

@pytest.mark.parametrize(p1.parameter_key, p1.parameter_value)
@pytest.mark.small
def test_mark2(x, y):
    time.sleep(0.1)
    assert x == y

@pytest.mark.parametrize(p1.parameter_key, p1.parameter_value)
@pytest.mark.large
def test_mark3(x, y):
    time.sleep(1)
    assert x == y

p2 = Parameters()
p2.get_params2()
of = Operate_File()

@pytest.mark.parametrize(p2.parameter_key, p2.parameter_value)
@pytest.mark.multi
def test_multiprocess1(cnt):
    log("cnt: {}".format(cnt))
    of.write_file("a"*(cnt+1))



# memo
# pytest --durations=0
# pytest -m small
# pytest -v
# pytest -n 2
# pytest --capture=no
