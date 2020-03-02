# 辞書 - キーと値のセットを扱う
# dict型 - 辞書を扱う型

# 辞書を作成
items = {'note': 1, 'notebook': 2, 'sketchbook': 3}
type(items)
print( type(items) )


items
print( items )


# キーワード引数を使った辞書の作成
dict(note=1, notebook=2, sketchbook=3)
print( dict(note=1, notebook=2, sketchbook=3) )



# 要素の追加と削除
items = {'note': 1, 'notebook': 2, 'sketchbook':3}


items['book'] = 4 # 要素を追加
items
print( items )


# items.pop('notebook') # 要素を取り出して辞書から削除
print( items.pop('notebook') )


print( items )


del items['sketchbook'] # 要素を削除

items
print( items )


# キーによる要素へのアクセス
items = {'note': 1, 'notebook': 2, 'soketchbook': 3}
items['note'] # キーを指定して値を取り出す
print( items['note'] )


# items['book'] # 存在しないキーを指定
#    items['book'] # 存在しないキーを指定
#    KeyError: 'book'


# get()を使うとキーがなくてもエラーにならない
# キーがない場合のデフォルト値はNone
items.get('book')

items.get('book', 0) # デフォルト値は変更できる
print( items.get('book', 0) )
