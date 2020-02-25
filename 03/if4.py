print(1 == 1) # 等価の場合にTrue

print(1 != 1) # 等価ではない場合にTrue

print(1 > 0) # 左辺が大きい場合にTrue

print(1 < 0) # 右辺が大きい場合にTrue

print(1 >= 0) # 左辺が大きいまたは等価の場合にTrue

print(1 <= 0) # 右辺が大きいまたは等価の場合にTrue

x, y, z = 1, 2, 3

# x < y and y < zと等価
print(x < y < z)

# x < y and y > zと等価
print(x < y > z) # 文法上は正しいが可読性は低い
