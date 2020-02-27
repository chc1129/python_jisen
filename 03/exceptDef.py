class PracticeBookError(Exception):
	"""モジュール独自の例外の基底クラス"""

class PageNotFoundError(PracticeBookError):
	"""ページが見つからないときの例外"""
	def __init__(self, message):
		self.message = message

class InvalidPageNumverError(PracticeBookError):
	"""不正なページ番号が指定されたときの例外"""
	def __init__(self, message):
		self.message = message


# fにファイルオブジェクトが代入される
with open('some.txt', 'w') as f:
	f.write('some txt')

# ファイルオブジェクトがクローズされていることを確認
f.closed


f = open('some.txt', 'w')
f.write('some text')

# ファイルオブジェクトはまだクローズされていない
f.closed

# ファイルオブジェクトを明示的にクローズ
f.close()
f.closed
