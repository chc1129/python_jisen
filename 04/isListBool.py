# 条件式で使える配列の性質
bool([]) # 空のリストは偽
print( bool([]) )


bool(['book']) # 要素があれば真
print( bool(['book']) )


'note' in ['note', 'notebook', 'sketchbook']
print( 'note' in ['note', 'notebook', 'sketchbook'] )


'book' not in ['note', 'notebook', 'sketchbook']
print( 'book' not in ['note', 'notebook', 'sketchbook'] )


empty = tuple()
bool(empty) # 空のタプルは偽
print( bool(empty) )


bool(('book',)) # 要素があれば真
print( bool(('book',)) )


'note' in ('note', 'noebook', 'sketchbook')
print( 'note' in ('note', 'noebook', 'sketchbook') )


'book' not in ('note', 'notebook', 'sketchbook')
print( 'book' not in ('note', 'notebook', 'sketchbook') )
