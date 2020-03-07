# クラスの継承

# メソッドのオーバーライドとsupper()による基底クラスへのアクセス
class Page:
	def __init__(self, num, content):
		self.num = num
		self.content = content
	def output(self):
		return f'{self.content}'

# メソッドのオーバーライド
class TitlePage(Page):
	def output(self):
		# 基底クラスのメソッドは自動では呼ばれないため
		# 明示的に呼び出す
		title = super().output()
		return title.upper()

title = TitlePage(0, 'Python Practice Book')
title.output()
print( title.output() )


# すべてのオブジェクトはobjectクラスのサブクラス
class Length(float): # 組み込み型のサブクラスを作成
	def to_cm(self):
		return super().__str__() + 'cm'

pencil_length = Length(16)
print(pencil_length.to_cm())



# 多重継承 - 複数の基底クラスを指定する
class HTMLPageMixin:
	def to_html(self):
		return f'<html><body>{self.output()}</body></html>'

# 多重継承を使ったMixinの利用
class WebPage(Page, HTMLPageMixin):
	pass

page = WebPage(0, 'web content')
page.to_html()
print( page.to_html() )



# 多重継承の注意点
class A:
	def hello(self):
		print('Hello')

class B(A):
	def hello(self):
		print('Hela')
		super().hello() # 基底クラスのメソッドを実行

class C(A):
	def hello(self):
		print('ニーハオ!')
		super().hello() # 基底クラスのメソッドを実行

class D(B, C):
	def hello(self):
		print('こんにちは')
		super().hello() # 基底クラスのメソッドを実行

d = D()
d.hello()



# __mro__属性を利用したメソッド解決順序の確認
D.__mro__ # メソッド解決順序を確認
print( D.__mro__ )


d.hello()

