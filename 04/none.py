None # 何も表示されない

print( str(None) ) # 文字列に変換すると'None'

print('book')

print( str(print('book')) ) # print() の戻り値はNone

d = {'a': 1, 'b': 2} # 辞書を定義
print (d.get('c') ) # 結果がNoneなので何も表示されない

print( d.get('a') )

