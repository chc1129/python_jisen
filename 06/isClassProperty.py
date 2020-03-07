# プロパティ - インスタンスメソッドをインスタンス変数のように扱う

class Book:
	def __init__(self, raw_price):
		if raw_price < 0:
			ValueError('price must be positive')
		self.raw_price = raw_price
		self._discounts = 0
	@property
	def discounts(self):
		return self._discounts
	@discounts.setter
	def discounts(self, value):
		if value < 0 or 100 < value:
			raise ValueError(
				'discounts must be between 0 and 100')
		self._discounts = value
	@property
	def price(self):
		multi = 100 - self._discounts
		return int(self.raw_price * multi / 100)

book = Book(2000)
book.discounts # 初期は値引率0
print( book.discounts )

book.price # 初期価格は2000
print( book.price )


book.discounts = 20 # 値引率を設定
book.price # 値引き後の価格
print( book.price )


# book.discounts = 120 # 100を超える値引率はエラー
#     File "isClassProperty.py", line 15, in discounts
#           raise ValueError(
#           ValueError: discounts must be between 0 and 100



# property - 値の取得時に呼び出されるメソッド

# Book クラス定義には, discounts()とprice()の2つの@propertyが付いた
# インスタンスメソッドが定義されています。このように、インスタンスメソッド
# に@propertyを付けると,そのインスタンスメソッドは()を付けずに呼び出せ
# ます。この@で始まる文字列でメソッドを修飾するPythonの機能をデコレータ
# と言います。



# setter - 値の設定時に呼び出されるメソッド

# Bookクラスには,@discounts.setterが付いたインスタンスメソッド
# discounts()も定義されています。これはsetterと呼ばれ,book.discounts =
# 20のように値を代入するときに呼ばれます。メソッド名には,@propertyを付
# けたメソッド名をそのまま利用しなければなりません。


# book.discounts = -20
#   File "isClassProperty.py", line 15, in discounts
#       raise ValueError(
#       ValueError: discounts must be between 0 and 100


# book.price = 1000
#   File "isClassProperty.py", line 67, in <module>
#       book.price = 1000
#       AttributeError: can't set attribute



# クラスやインスタンスのプライベートな属性

# アンダースコアから始まる属性

book._discounts # _で始まる変数も参照できる
print( book._discounts )


# アンダースコア2つから始まる属性
class Klass:
	def __init__(self, x):
		self.__x = x

kls = Klass(10)
# kls.__x # この名前では参照できない
#  File "isClassProperty.py", line 88, in <module>
#      kls.__x # この名前では参照できない
#      AttributeError: 'Klass' object has no attribute '__x'


kls._Klass__x # 変換規則を知っていれば参照できる
print( kls._Klass__x )


# プライベートな属性に対するPythonコミュニティの考え方

