type(3.0)
print( type(3.0) )

type(1e-5) # 指数表記にも対応(eはEでも可)
print( type(1e-5) )

3.0 + 4.0 # float型どうしの演算はfloat型
print( 3.0 + 4.0 )

infinity = float('inf') # 無限大

type(infinity) # 無限大はfloat型
print( type(infinity) )

infinity + 1 # 無限大を含む演算
print( infinity + 1 )

float('-inf') # 負の無限大
print( float('-inf') )

nan = float('nan')
print( float('nan') ) # NaN

type(nan) # NaNもfloat型
print( type(nan) )

nan + 1 # NaNを含む演算
print( nan + 1 )


import sys

sys.float_info
print( sys.float_info )


