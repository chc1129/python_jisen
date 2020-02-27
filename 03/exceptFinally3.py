f = open('some.txt', 'r')
try:
	# 読み取りモードなので書き込めない
	f.write('egg')
finally:
	print('ファイルをクローズします')
	f.close()
