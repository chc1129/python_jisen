x = 'book'
y = 'note'
print(x == y) # 等価の場合にTrue

print(x != y) # 等価でない場合にTrue

print(x is None) # 同じオブジェクトの場合にTrue

print(x is not None) # 同じオブジェクトでない場合にTrue

# itemsはリスト
items = ['book', 'note']

# itemsに'book'が含まれている場合にTrue
print('book' in items)

# itemsに'book'が含まれていない場合にTrue
print('book' not in items)

# countは辞書
count = {'book':1, 'note':2}

print('book' in count) # 辞書の場合はキーを用いて判定される

print(1 in count)
