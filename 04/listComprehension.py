# 内包表記 - 効率的なシーケンスの生成
# リスト内包表記 - 効率的なリストの生成

numbers = []
for i in range(10):
	numbers.append(str(i))

numbers
print( numbers )


[str(v) for v in range(10)]
print( [str(v) for v in range(10)] )


# 先ほどのfor文で使った変数iが定義されている
i
print( i )


# 内包表記で使った変数vは外側には定義されていない
#v
# print( v )
#    v
#    NameError: name 'v' is not defined


# ネストしたリストの内包表記
tuples = []
for x in [1, 2, 3]:
	for y in [4, 5, 6]:
		tuples.append((x, y))

tuples
print( tuples )


[(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print( [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]] )



# if 文のある内包表記
even = []
for i in range(10):
	if i % 2 == 0:
		even.append(i)

even
print( even )



[x for x in range(10) if x % 2 == 0]
print( [x for x in range(10) if x % 2 == 0] )



# そのほかの内包表記
set_comprehension = {i for i in range(10)}
type(set_comprehension)
print( type(set_comprehension) )



set_comprehension
print( set_comprehension )


dict_comprehension = {str(x): x for x in range(3)}
type( dict_comprehension )
print( type( dict_comprehension ) )


dict_comprehension
print( dict_comprehension )


gen = (i for i in range(3))
type(gen)
print( type(gen) )


gen
print( gen )
