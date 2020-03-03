# 関数 - 関連する処理をまとめる
# 関数の定義と実行

def print_page(): # 関数を定義
	print('no content')

print_page() # 関数を実行



# 引数を取る関数

def print_page(content):
	print(content)

print_page('my contents') # 引数を渡して関数を実行


# 引数のない呼び出しはエラー
# print_page()
#     print_page()
#     TypeError: print_page() missing 1 required positional argument: 'content'


def print_page(content='no content'):
	print(content)

print_page() # デフォルト値が利用される

# 引数を渡すとその値が利用される
print_page('my contents')



# 関数はオブジェクト

def print_page(content='no content'):
	print(content)

# 変数print_pageは関数オブジェクト
type(print_page)
print( type(print_page) )


f = print_page # 変数fに関数print_pageを代入
f() # print_page()と同等


def print_title(printer, title):
	print('@@@@@')
	# 引数printerは関数オブジェクト
	printer(title.upper())
	print('@@@@@')


# 関数print_pageを渡し、タイトルを印刷
print_title(print_page, 'python practice book')



# 関数の戻り値
def increment(page_num):
	return page_num + 1

next_page = increment(1) # 戻り値をnext_pageに格納
next_page
print( next_page )


# 内側のincrement(2)の戻り値3が外側のincrementの引数になる
increment(increment(next_page))
print( next_page )



def increment(page_num, last):
	next_page = page_num + 1
	if next_page <= last:
		return next_page
	raise ValueError('Invalid arguments')


increment(1, 3) # returnで処理は終了する


# increment(3, 3) # returnされないため最後まで実行される
#    raise ValueError('Invalid arguments')
#    ValueError: Invalid arguments



# returnがない場合の戻り値
def no_value(): # return文に値を渡さない関数
	return

	print(no_value()) # 戻り値はNone


def no_return(): # return文がない関数
	pass

print(no_return())


# 条件によってreturn文が実行されない場合がある関数
def increment(page_num, last):
	next_num = page_num + 1
	if next_num <= last:
		return next_num

next_page = increment(3, 3) # return文が実行されない
print(next_page) # 戻り値はNone



