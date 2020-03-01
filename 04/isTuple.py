# tuple型 - 不変な配列を扱う型
# タプルを作成
items = ('note', 'notebook', 'sketchbook')
type(items)
print( type(items) )


items
print( items )


# ()はなくてもよい
items = 'note', 'notebook', 'sketchbook'
items
print( items )


# リストからタプルを作成
items = ['note', 'notebook']
tuple(items)
print( tuple(items) )



# タプル作成時の注意点
tuple() # 空のタプル
print( tuple() )


() # これも空のタプル
print( () )


# (,) # これは間違い
# print( (,) )


items = 'note', # 要素が1つのタプルを作成
items
print( items )


# 戻り値がタプルになっている
def add(a, b):
	# タイプミスによりカンマ(,)が付いた
	return a + b

1 + add(2, 3)
print( 1 + add(2, 3) )


# インデックスによる要素へのアクセス
items = ('note', 'notebook', 'sketchbook')
items[1]
print( items[1] )


# items[1] = 'book' # 要素の変更はできない
#    items[1] = 'book' # 要素の変更はできない
#    TypeError: 'tuple' object does not support item assignment


# 要素数以上のインデックスはエラー
# items[10]
# print( items[10] )
#    items[10]
#    IndexError: tuple index out of range


# スライスによるタプルの切りだし
items = ('note', 'notebook', 'sketchbook')
items[0:2] # 先頭からitems[2]の1つ前までが含まれる
print( items[0:2] )


items[:2] # :の前を省略すると先頭から
print( items[:2] )


items[1:] # :の後を省略すると最後まで
print( items[1:] )


# 選択した部分の置き換えはできない
items[0:2] = (1, 2)
#    items[0:2] = (1, 2)
#    TypeError: 'tuple' object does not support item assignment
