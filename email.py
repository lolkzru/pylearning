x = input()
if '@' in x:
	if '.com' in x or '.ru' in x:
		print('YES')
	else:
		print('NO')
else:
	print('NO')