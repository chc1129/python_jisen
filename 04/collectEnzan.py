# 集合の演算 - 和, 積, 差, 対称差

set_a = {'note', 'notebook', 'sketchbook'}
set_b = {'book', 'rulebook', 'sketchbook'}

set_a | set_b # 和集合
print( set_a | set_b )


# 差集合, set.difference()でも同様
set_a - set_b
print( set_a - set_b )


# 積集合, set.intersection()でも同様
set_a & set_b
print( set_a & set_b )


# 対称差, set.symmetric_difference()でも同様
set_a ^ set_b
print( set_a ^ set_b )


# 部分集合か判定, set.issubset()でも同様
{'note', 'notebook'} <= set_a
print( {'note', 'notebook'} <= set_a )
