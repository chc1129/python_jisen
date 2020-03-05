# Pythonのクラス機構

# classキーワードによるクラスの定義
class Page: # クラスの定義
	def __init__(self, num, content):
		self.num = num # ページ番号
		self.content = content # ページの内容
	def output(self):
		return f'{self.content}'

Page # クラスオブジェクトPageが定義された
print( Page )


# インスタンスの作成

# インスタンス化
title_page = Page(0, 'Python Practice Book')

type(title_page) # インスタンスのクラスを確認
print( type(title_page) )

# Pageクラスのインスタンスか確認
isinstance(title_page, Page)
print( isinstance(title_page, Page) )


# インスタンスが持つ属性を確認
dir(title_page)
print( dir(title_page) )



# インスタンス - クラスをもとに生成されるオブジェクト

# インスタンスメソッド - インスタンスに紐付くメソッド
title_page.output() # インスタンスメソッドの呼び出し
print( title_page.output() )


# メソッドオブジェクトと関数オブジェクト
class Klass:
	def some_method(self): # インスタンスメソッドを定義
		print('method')

def some_function(self): # 同じ引数の関数を定義
	print('function')


# 関数はfunctionクラスのインスタンス
type(some_function)
print( type(some_function) )


# インスタンスメソッドもfunctionクラスのインスタンス
type(Klass.some_method)
print( type(Klass.some_method) )


# インスタンスを通じてアクセスするとmethodクラスになる
kls = Klass()
type(kls.some_method)
print( type(kls.some_method) )


# クラスオブジェクトの属性に関数を追加
Klass.some_function = some_function

# インスタンスメソッドとして実行
kls.some_function()
print( kls.some_function() )


# インスタンス変数 - インスタンスが保持する変数
title_page.section = 0
title_page.section
print( title_page.section )


first_page = Page(1, 'first page')
first_page.section
#     first_page.section
# 	AttributeError: 'Page' object has no attribute 'section'
