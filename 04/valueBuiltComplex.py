a = 1.2 + 3j
a
print( a )


type(a)
print( type(a) )


a.real # 実部を取得
print( a.real )


a.imag # 虚部を取得
print( a.imag )


a + 2j # complex型どうしの演算はcomplex型
print( a + 2j )

a + 2 # complex型とint型の演算はcomplex型
print( a + 2 )

a + 3.4 # complex型とfloat型の演算もcomplex型
print( a + 3.4 )
