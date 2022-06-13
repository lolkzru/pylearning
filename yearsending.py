x = int(input())
d1 = x // 1000
d2 = (x // 100) % 10
d3 = (x // 10) % 10
d4 = x % 10
if d3 == 0 and d4 == 0:
	print('YES')
else:
	print('NO')