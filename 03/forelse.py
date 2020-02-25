# 奇数がなければメッセージを表示
nums = [2, 4, 6, 8]
for n in nums:
	if n % 2 == 1:
		break
else:
	print('奇数の値を含めてください')
