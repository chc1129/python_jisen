# 文字列の作成
# 'book'でも同じ
book = 'book'
type(book)

print( type(book) )


# 改行(\n)を含む文字列の作成
notebook = 'note\nbook'
print(notebook) # print()を使うと改行して出力される


# 3つの区オートでくくると通常の改行も含められる
notebook = """
note
book
"""
print(notebook)



# ()でくくるだけで、,や+は付けない
URL = ('https://gihyo.jp'
			'/magazine/wdpress/archive'
			'/2018/vol104')

print(URL)


book = 'book'
'note' + book

print( 'note' + book )


book * 4
print( book * 4 )


book # もとの文字列はそのまま
print( book )
