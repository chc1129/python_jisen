# インスタンスの初期化
# __init__() - インスタンスの初期化を行う特殊メソッド

# クラスの定義
class Page:
	def __init__(self, num, content, section=None):
		self.num = num
		self.content = content
		self.section = section
	def output(self):
		return f'{self.content}'


# 引数を渡してインスタンス化する
# インスタンスを作成
title_page = Page(0, 'Python Practice Book')

title_page.section # sectionはNone

title_page.output()
print( title_page.output() )

# sectionを指定して別のインスタンスを作成
first_page = Page(1, 'fist page', 1)

first_page.section # sectionが指定されている

first_page.output()
print( first_page.output() )



# __init__()と__new__()の違い - イニシャライザとコンストラクタ

class Klass:
	def __new__(cls, *args): # コンストラクタ
		print(f'{cls}')
		print('new', args)
		# 作成したインスタンスを返す
		return super().__new__(cls)
	def __init__(self, *args):
		# インスタンスの初期化はこちらで行う
		print('init', args)

# クラスオブジェクトの呼び出し
kls = Klass(1, 2, 3)


# __new__()の注意点
class Evil:
	def __new__(cls, *args):
		return 1

# Evilクラスをインスタンス化
evil = Evil()

isinstance(evil, Evil)
print( isinstance(evil, Evil) )


type(evil)
print( type(evil) )


# インスタンスは__new__()の戻り値
evil
print( evil )


class MyClass(Evil):
	def print_class(self):
		print('MyClass')

my = MyClass() # myの値は1になる

# 追加したはずのメソッドが利用できない
my.print_class()
#    my.print_class()
#    AttributeError: 'int' object has no attribute 'print_class'

my
print( my )
