# 集合 - 一意な要素の集合を扱う
# set型 - 可変な集合を扱う型

# set型の集合を作成
items = {'note', 'notebok', 'sketchbook'}
type(items)
print( type(items) )


items
print( items )


# 重複している要素は1つになる
set (['note', 'notebook', 'sketchbook', 'sketchbook'])
print( set (['note', 'notebook', 'sketchbook', 'sketchbook']) )



set() # 空のset型を作成
print( set() )



# 順序がないためインデックスでの参照は不可
items = {'note', 'notebook', 'sketchbook'}
# items[0]
#    items[0]
#    TypeError: 'set' object is not subscriptable



# 要素の追加と削除
items = {'note', 'notebook', 'sketchbook'}
items.add('book') # 要素を追加
items
print( items )


# 要素を指定して削除
items.remove('book')
items
print( items )


# 要素を取り出して集合から削除
# 順序がないため取り出される要素は不定
#items.pop()
print( items.pop() )


items
print( items )
