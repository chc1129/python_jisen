# 配列 - 要素を一列に並べて扱う
# list型 - 可変な配列を扱う型

# リストを作成
items = ['note', 'notebook', 'sketchbook']
type(items)
print( type(items) )

items
print( items )


# 文字列はイテラブルなオブジェクト
list('book')
print( list('book') )



# 要素の追加と削除
items = ['note', 'notebook', 'sketchbook']

items.append('paperbook') # 要素を追加
print( items )

items = ['book'] + items # リストの結合
print( items )

items.pop(0) # 先頭の要素を取り出してリストから削除
print( items.pop(0) )


items
print( items )


del items[1] # 要素を削除
items
print( items )


# インデックスによる要素へのアクセス
items = ['note', 'notebook', 'sketchbook']

items[1] # インデックスは先頭を0として右向きに数える
print( items[1] )


items[-2] # 負の値の場合,末尾を-1として左向きに数える
print( items[-2] )


items[1] = 'book'
items
print( items )


# items[10] # 要素範囲外のインデックスはエラー
# print( items[10] )



# スライスによるリストの切り出し
items = ['note', 'notebook', 'sketchbook']

items[0:2] # 先頭からitems[2]の1つ前までが含まれる
print( items[0:2] )


items # もとのリストはそのまま
print( items )


items[:2] # :の前を省略すると先頭から
print( items[:2] )

items[1:] # :1の後を省略すると最後まで
print( items[1:] )


items = ['note', 'notebook', 'sketchbook' ]
items[0:-1]
print( items[0:-1] )


# 要素数は一致していなくてもよい
items = ['note', 'notebook', 'sketchbook']
items[0:2] = [1, 2, 3]
items
print( items )
