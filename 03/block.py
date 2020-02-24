import sys

def py2_or_py3():
	# インデントが下がっている
	# 実行中のPythonのバージョンを取得
	major = sys.version_info.major
	if major < 3:
		# さらにインデントが下がっている
		return 'Python 2'
	else:
		# 同じくインデントが下がっている
		return 'Python 3'
