# str型とよく似たbytes型
# str.encode()とbytes.decode()を利用した相互変換

book = 'Python実践入門'
type(book)
print( type(book) )

book # 文字列を表示
print( book )


# UTF-8を指定してエンコード
encoded = book.encode('utf-8')
type(encoded) # bytesになっていることを確認
print( type(encoded) )


encoded # バイト列を表示
print( encoded )


# 正しいエンコーディングを指定してデコード
encoded.decode('utf-8')
print( encoded.decode('utf-8') )


# 誤ったエンコーディングを指定するとエラー
# encoded.decode('shift-jis')
# print( encoded.decode('shift-jis') )
