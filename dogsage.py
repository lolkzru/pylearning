x = float(input())
a = 0
if 1 <= x <= 2:
	a = x * 10.5
elif x > 2:
	a = ((x - 2) * 4) + (2 * 10.5)
print(a)