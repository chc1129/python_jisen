# for文での辞書の挙動
items = {'note': 1, 'notebook': 2, 'sketchbook': 3}
for key in items: # キーだけを取得
	print(key)



items = {'note': 1, 'notebook': 2, 'sketchbook': 3}
for value in items.values(): # 値だけを取得
	print(value)



# キー値のタプルを取得
for key, value in items.items():
	print(key, value)



# 条件式で使える辞書の性質
bool({}) # 空の辞書は偽
print( bool({}) )


bool({'book': 0}) # 要素があれば真
print( bool({'book': 0}) )


items = {'note': 1, 'notebook': 2, 'sketchbook': 3}
'note' in items
print( 'note' in items )


'book' not in items
print( 'book' not in items )


1 in items # in演算子はキーで判定
print( 1 in items )



1 in items.values() # 値に対してin演算子を利用
print( 1 in items.values() )




