def py2_or_py3():
		"""実行中のPythonが2系か3系かを判定する

		この関数はPython 1.xでの実行は想定しない
		"""
	major = sys.version_info.major
	if major < 3:
		return 'Python 2'
	else:
		return 'Python 3'
