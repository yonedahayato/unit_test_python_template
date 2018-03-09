import sys
from unittest import TestCase, main
import unittest

class test_name(TestCase):
    # 各テスト前に呼び出される
    # DBのセットアップやテストデータの準備などを行う
    one = 1
    two = 2
    three = 3

    @classmethod
    def setUpClass(cls):
        print('*** 全体前処理 ***')
        cls.one = 1
        cls.check_data_dict = {"data_name": [], "data":[]}
        # test_name.check_data_dict["data_name"].append("data_name1")
        # test_name.check_data_dict["data"].append(data1)

    def setUp(self):
        print('+ テスト前処理')

    # 各テスト後に呼び出される
    # テストの後処理（成果物の削除）やDB処理の後処理などを行う
    def tearDown(self):
        print('+ テスト後処理')

    @classmethod
    def tearDownClass(cls):
        print('*** 全体後処理 ***')
        print("cls.three is {}".format(cls.three))

        if len(cls.check_data_dict["data_name"]) == len(cls.check_data_dict["data"]) and \
            len(cls.check_data_dict["data_name"]) != 0:

            for Index in range(len(cls.check_data_dict["data_name"])):
                print(cls.check_data_dict["data_name"][Index])
                print(cls.check_data_dict["data"][Index])
        else:
            print("check_data`s is invalid length.")

    @classmethod
    def compare_data(self, data_name1, data_name2):
        data1, data2 = None, None
        for Index in range(len(cls.check_data_dict["data_name"])):
            if cls.check_data_dict["data_name"][Index] == "data_name1":
                data1 = cls.check_data_dict["data"][Index]
            if cls.check_data_dict["data_name"][Index] == "data_name2":
                data2 = cls.check_data_dict["data"][Index]

        if data1 == None or data2 == None:
            print("fail to compare")

        else:
            print("compare_check:{}".format(data1 == data2))

    def test_do_something(self):
        print("test_do_something")
        one = self.one
        self.assertEqual(one, 1, "one is 1")

    def test_do_otherthing(self):
        print("test_do_otherthing")
        two = self.two
        self.assertTrue(two == 2, "two is 2")

    @unittest.skip("skip message <skipもできる>")
    def test_skip(self):
        print("skip")

    def test_subTest(self):
        def same_value(x):
            return x

        for i in range(10):
            with self.subTest(arg_1=1, arg2=2):
                self.assertEqual(same_value(i), i)

if __name__ == "__main__":
    unittest.main()
