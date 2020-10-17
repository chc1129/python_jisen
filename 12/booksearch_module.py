import unittest

# アプリケーションコード
def booksearch():
	# 任意の処理
	return {}

class BookSearchTest(unittest.TestCase):
	# booksearch()のテストコード
	def test_booksearch(self):
		self.assertEqual({}, booksearch())

if __name__ == '__main__':
	unittest.main()
