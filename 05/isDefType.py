# 型ヒント - アノテーションで関数に型情報を付与する
# 型情報を付与するのメリット

# OptionalはNoneの可能性がある場合に利用
from typing import Optional

def increment(
	page_num: int,
	last: int,
	*,
	ignore_error: bool = False) -> Optional[int]:
	next_page = page_num + 1
	if next_page <= last:
		return next_page
	if ignore_error:
		return None
	raise ValueError('Invalid arguments')

increment.__annotations__ # 型情報が格納されている
print( increment.__annotations__ )


# 実行時の型チェックはされないためエラーにはならない
increment(1, 3, ignore_error=1)
print( increment(1, 3, ignore_error=1) )


# 変数への型情報の付与
def decrement(page_num: int) -> int:
	prev_page: int # 型情報を付けて変数を宣言
	prev_page = page_num - 1
	return prev_page

decrement(2)
print( decrement(2) )

# 実行時の型チェックはされないためエラーにはならない
decrement(2.0)
print( decrement(2.0) )


# 型ヒントの活用例 - 静的解析ツールの利用
# !cat scratch.py

# mypyコマンドによる静的型チェックの実行
# !docker run -it --rm -v $(pwd):/usr/src/app -w /usr/src/app python:3.8.1 bash -c 'pip install mypy=0.740; mypy scratch.py'

