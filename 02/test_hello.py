# unittestモジュールを読み込んで利用
import unittest

class TestFunc(unittest.Testcase):
	def test_func(self):
		from hello import func
		self.assertIsNone(func('こんにちは'))
