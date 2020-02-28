# bool型はTrueとFalseのみ
print( type(True) )

print( type(False) )

print( bool(None) ) # どのようなオブジェクトでも真理値判定が行える

print( bool([]) ) # 空のコンテナオブジェクトは偽

print( bool(['book']) ) # 偽にならないものはすべて真
