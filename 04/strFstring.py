# 文字列の変数置換
# f-string -- 式を埋め込める
title = 'book'

f'python practive {title}' # 変数の値で置換
print( f'python practive {title}' )


f'python practice {"note" + title}' # 式を利用
print( f'python practice {"note" + title}' )


def print_title():
	print(f'python practice {title}')

print_title()


title = 'sketchbook'
print_title() # f-stringは実行時に評価される


note = 'note'

# Python 3.7まで
f'title={title}, note={note}'
print( f'title={title}, note={note}' )

# Python 3.8以降はシンプルに書ける
f'{title=}, {note=}'
print( f'{title=}, {note=}' )


# 属性や式にも利用できる
f'{title.upper()=}'
print( f'{title.upper()=}' )
