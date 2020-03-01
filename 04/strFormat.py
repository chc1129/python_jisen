# 渡した順で置換
'python {} {}'.format('practice', 'book')
print( 'python {} {}'.format('practice', 'book') )


# 引数の位置を指定して置換
'python {1} {0}'.format('book', 'practice')
print( 'python {1} {0}'.format('book', 'practice') )


# キーワードを指定して置換
'python {p} {b}'.format(b='book', p='practive')
print( 'python {p} {b}'.format(b='book', p='practive') )


# 辞書を定義
d = {'x': 'note', 'y': 'notebook', 'z': 'sketchbook'}

# 使わないキーがあってもよい
books = '{x} {z}'
books.format(**d)
print( books.format(**d) )


# %演算子 - 一番古い文字列フォーマット
book = 'book'
'note%s' % (book) # %sを置換
print( 'note%s' % (book) )


# %sは文字列, %dは10進整数に対応
'python practice %s: %d' % (book, 1.0)
print( 'python practice %s: %d' % (book, 1.0) )
