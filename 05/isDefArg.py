# 関数のさまざまな引数
# 位置引数 - 仮引数名を指定しない実引数の受け渡し
def increment(page_num, last):
	next_page = page_num + 1
	if next_page <= last:
		return next_page
	raise ValueError('Invalid argument')

increment(2, 10) # 位置引数による関数呼び出し
print( increment(2, 10) )


# 実引数が足りない
# increment(2)
#     increment(2)
#     TypeError: increment() missing 1 required positional argument: 'last'


# 実引数が多い
# increment(2, 10, 1)
#    increment(2, 10, 1)
#    TypeError: increment() takes 2 positional arguments but 3 were given



# デフォルト値のある引数- 呼び出し時に実引数を省略できる引数

# lastにデフォルト値を指定
def increment(page_num, last=10):
	next_page = page_num + 1
	if next_page <= last:
		return next_page

# この呼び出しではlastはデフォルト値の10
increment(2)
print( increment(2) )


# この呼び出しではlastは実引数で渡した1
increment(2, 1)
print( increment(2, 1) )


# デフォルト値のある引数は位置引数より後ろでないといけない
# def increment(page_num=0, last):
# 	pass
#     def increment(page_num=0, last):
#                   ^
# SyntaxError: non-default argument follows default argument


# デフォルト値の落とし穴
from datetime import datetime

# これはデフォルト値の間違った使い方の例
def print_page(content, timestamp=datetime.now()):
	print(content)
	print(timestamp)

print_page('my content')

# タイムスタンプが2回目とまったく同じ
print_page('my content 2')


# デフォルト値はNoneにする
def print_page(content, timestamp=None):
	if timestamp is None:
		timestamp = datetime.now()
	print(content)
	print(timestamp)

print_page('my content')


# 実行時の現在時刻が表示される
print_page('my content 2')


# 可変長の位置引数
# 可変長の位置引数を受け取る
def print_pages(content, *args):
	print(content)
	for more in args:
			print('more:', more)

print_page('my content') # argsは空のタプル

# argsは('content2', 'content3')
print_pages('my content', 'content2', 'content3')


# 可変長のキーワード引数
# 可変長のキーワード引数を受け取る
def print_page(content, **kwargs):
	print(content)
	for key, value in kwargs.items():
		print(f'{key}: {value}')


print_page('my content', published=2019, author='rei suyama')


# どのような呼び出しにも対応
def print_pages(*args, **kwargs):
	for content in args:
		print(content)
	for key, value in kwargs.items():
		print(f'{key}: {value}')

print_pages('content1', 'content2', 'content3',
	published=2019, author='rei suyama')



# キーワードのみ引数 - 呼び出し時に仮引数が必須になる引数
# *以降がキーワードのみ引数になる
def increment(page_num, last, *, ignore_error=False):
	next_page = page_num + 1
	if next_page <= last:
		return next_page
	if ignore_error:
		return None
	raise ValueError('Invalid arguments')

# キーワード引数でのみ指定できる
increment(2, 2, ignore_error=True)

# increment(2, 2, True) # 位置引数ではエラーになる
#    increment(2, 2, True) # 位置引数ではエラーになる
#    TypeError: increment() takes 2 positional arguments but 3 were given


# 位置のみ引数 - 呼び出し時に仮引数名を指定できない引数
abs(-1) # abs()は位置のみ引数の例
print( abs(-1) )


# ヘルプページはqで終了
# help(abs)


# abs(x=1) # 仮引数名を指定するとエラー
#     abs(x=1) # 仮引数名を指定するとエラー
#     TypeError: abs() takes no keyword arguments


# /より前が位置のみ引数になる
def add(x, y, /, z):
	return x + y + z

add(1, 2, 3)
print( add(1, 2, 3) )


# zはキーワードでも指定できる
add(1, 2, z=3)
print( add(1, 2, z=3) )


# xとyはキーワードでは指定できない
# add(x=1, y=2, z=3)
#     add(x=1, y=2, z=3)
#     TypeError: add() got some positional-only arguments passed as keyword arguments: 'x, y'


# 引数リストのアンパック - リストや辞書に格納された値を引数に渡す
def print_page(one, two, three):
	print(one)
	print(two)
	print(three)

contents =['my content', 'content2', 'content3']

# print_page('my content', 'content2', 'content3')と同じ
print_page(*contents) # 引数リストのアンパック


def print_page(content, published, author):
	print(content)
	print('published:', published)
	print('author:', author)

footer = {'published': 2019, 'author': 'rei suyama'}

# 辞書の値をキーワード引数として渡す
print_page('my content', **footer)



# 関数のDocstring
def increment(page_num, last, *, ignore_error=False):
	"""次のページ番号を返す

	:param page_num: もとのページ番号
	:type page_num: int
	:param last: 最終ページの番号
	:type last: int
	:param ignore_error: Trueの場合ページのオーバーで例外を送出しない
	:type ignore_error: bool
	:rtype: int
	"""

	next_page = page_num + 1
	if next_page <= last:
		return next_page
	if ignore_error:
		return None
	raise ValueError('Invalid arguments')
