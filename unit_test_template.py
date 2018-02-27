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

    def setUp(self):
        print('+ テスト前処理')

    # 各テスト後に呼び出される
    # テストの後処理（成果物の削除）やDB処理の後処理などを行う
    @classmethod
    def tearDownClass(cls):
        print('*** 全体後処理 ***')
        print("cls.three is {}".format(cls.three))

    def tearDown(self):
        print('+ テスト後処理')

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

if __name__ == "__main__":
    unittest.main()
