# ファイルを読み取りモードでオープン
f = open('some.txt', 'r')
try:
	print(f.read())
finally:
	print('ファイルをクローズします')
	f.close()
