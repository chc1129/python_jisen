# どちらか一方でも真であれば真
print( True or True )

print( True or False )

print( False or True )

print( False or False )

x = ['book']
y = []
print( x or y ) # xが真なのでxが返る

print( y or y ) # 入れ替えてもyが偽なのでxが帰る

z = 0
print( y or z) # 両方偽なのでzが返る

print( z or y) # 入れ替えるとyが返る
