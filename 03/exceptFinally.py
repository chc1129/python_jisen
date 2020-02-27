# 作成されるsome.txtは次項に進む前に削除する
from io import UnsupportedOperation

# ファイルを書き込みモードでオープン
f = open('some.txt', 'w')
try:
	# 書き込みモードなので読み込めない
	f.read()
except UnsupportedOperation as e:
	print(f'例外が発生しました: {e}')
finally:
	print('ファイルをクローズします')
	f.close()
