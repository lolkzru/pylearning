z = int(input())
a = z // 100
b = (z % 100) // 10
c = z % 10
d = (max(a, b, c))
e = ((a + b + c) - (max(a, b, c) + (min(a, b, c))))
f = ((min(a, b, c)))
if (d - f == e):
	print('Число интересное')
else:
	print('Число неинтересное')
