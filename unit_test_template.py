import sys
from unittest import TestCase, main
import unittest

class test_name(TestCase):
    # 各テスト前に呼び出される
    # DBのセットアップやテストデータの準備などを行う
    def setUpClass():
        print('*** 全体前処理 ***')

    def setUp(self):
        print('+ テスト前処理')

    # 各テスト後に呼び出される
    # テストの後処理（成果物の削除）やDB処理の後処理などを行う
    def tearDownClass():
        print('*** 全体後処理 ***')

    def tearDown(self):
        print('+ テスト後処理')

    def test_do_something(self):
        print("test_do_something")
        one = 1
        self.assertEqual(one, 1, "one is 1")

    def test_do_otherthing(self):
        print("test_do_otherthing")
        two = 2
        self.assertTrue(two == 2, "two is 2")

if __name__ == "__main__":
    unittest.main()
