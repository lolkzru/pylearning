y = int(input())
x = int(input())
y1 = int(input())
x1 = int(input())

ynew = y1 - y
xnew = x1 - x

if (xnew > 0 and ynew > 0) or (xnew > 0 and ynew < 0) or (xnew < 0 and ynew > 0) or (xnew < 0 and ynew < 0):
    print('YES')
else:
    print('NO')
