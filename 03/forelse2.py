# 奇数のがあれば何も出力されない
nums = [2, 4, 6, 7, 8]
for n in nums:
	if n % 2 == 1:
		break
else:
	print('奇数の値を含めてください')
