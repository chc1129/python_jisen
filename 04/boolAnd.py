# 両方が真なら真
print( True and True )

print( True and False )

print( False and True )

print( False and False )

x = ['book']
y = []
print( x and y ) # xが真なのでyが返る

print( y and x ) # yが偽なのでyが返る

z = 1
print( x and z ) # 両方真なのでzが返る

print( z and x ) # 入れ返るとxが返る
