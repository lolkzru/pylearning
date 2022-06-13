a = int(input())
b = int(input())
c = str(input())

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    C = '//'
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        b = float(b)
        print(a // b)
elif c == '*':
    print(a * b)

else:
    print('Неверная операция')

