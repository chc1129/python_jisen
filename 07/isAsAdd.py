open # 組み込み関数のopen
print( open )


from gzip import open # gzipのopenをインポート
open # open()はgzip.open()になっている
print( open )


# gzipのopenをgzip_openとしてインポート
from gzip import open as gzip_open
gzip_open # gzipのopen
print( gzip_open )
