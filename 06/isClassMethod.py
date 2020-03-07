# クラスメソッド - クラスに紐付くメソッド

# 属性を使ったソートに使える標準ライブラリをインポート
from operator import attrgetter

class Page:
	book_title = 'Python Practice Book'
	def __init__(self, num, content):
		self.num = num
		self.content = content
	def output(self):
		return f'{self.content}'
	# クラスメソッドの第1引数はクラスオブジェクト
	@classmethod
	def print_pages(cls, *pages):
		# クラスオブジェクトの利用
		print(cls.book_title)
		pages = list(pages)
		# ページ順に並べ替えて出力
		for page in sorted(pages, key=attrgetter('num')):
			print(page.output())

first = Page(1, 'first page')
second = Page(2, 'second page')
third = Page(3, 'third page')


# クラスメソッドの呼び出し
Page.print_pages(first, third, second)


# インスタンスからも呼び出せる
first.print_pages(first, third, second)


# スタティックメソッド - 関数のように振る舞うメソッド

class Page:
	def __init__(self, num, content):
		self.num = num
		self.content = content
	@staticmethod # スタティックメソッドにする
	def check_blank(page):
		return bool(page.content)

page = Page(1, '')
Page.check_blank(page)
print( Page.check_blank(page) )


def check_blank(page): # 関数で問題ない
	return bool(page.content)

check_blank(page)
print( check_blank(page) )
