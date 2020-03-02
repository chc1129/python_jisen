# for文での集合の挙動
items = {'note', 'notebook', 'sketchbook'}
items
print( items )


for item in items:
	print(item)


# frozenset型でも同様
frozen_items = frozenset(items)
items
print( items )

for item in frozen_items:
	print(item)


# 条件式で使える集合の性質
bool(set()) # 空の場合は偽
print( bool(set()) )


# 要素があれば真
items = {'note', 'notebook', 'sketchbook'}
bool(items)
print( bool(items) )


'note' in items
print( 'note' in items )


'book' not in items
print( 'book' not in items )


# frozenset型も同様
bool(frozenset())
print( bool(frozenset()) )


frozen_items = frozenset(items)
frozen_items
print( frozen_items )


# 要素があれば真
bool(frozen_items)
print( bool(frozen_items) )


'note' in frozen_items
print( 'note' in frozen_items )


'book' not in frozen_items
print( 'book' not in frozen_items )
