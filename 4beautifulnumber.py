num = int(input())
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10
if (1000 <= num <= 9999) and (1 <= d1 <= 9) and (0 <= d2 <= 9) and (0 <= d3 <= 9) and (0 <= d4 <= 9) and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')

