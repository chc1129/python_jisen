# lambda式 - 無名関数の作成

increment = lambda num: num + 1 # lambda式で関数を定義

increment # lambda式であることがわかる
print( increment )

increment(2)
print( increment(2) )


# このlambda式と同等の通常の関数定義
def increment(num):
	return num + 1


# lambda式の使いどころ
nums = ['one', 'two', 'three']

# 第1引数の関数が真になるもののみが残る
filtered = filter(lambda x: len(x) == 3, nums)
#list(filtered)
print( list(filtered) )


