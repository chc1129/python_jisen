def py2_or_py3():
	major = sys.version_info.major
	if major < 3:
		# Python 1.xでの実行は想定しない
		return 'Python 2'
	else:
		return 'Python 3'
