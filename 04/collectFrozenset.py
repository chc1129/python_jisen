# frozenset型 - 不変な集合を扱う型

# frozenset型の集合を作成
items = frozenset(['note', 'notebook', 'sketchbook'])
type(items)
print( type(items) )


# set型と同様, 要素の重複を許さず,順序も保持しない
items
print( items )


# 不変な型なので変更はできない
# items.add('book')
#    items.add('book')
#    AttributeError: 'frozenset' object has no attribute 'add'
