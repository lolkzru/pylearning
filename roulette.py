x = int(input())
if 0 < x <= 36:
    if 1 <= x <= 10:
        if x % 2 == 0:
            print('черный')
        else:
            print('красный')
    if 11 <= x <= 18:
        if x % 2 == 0:
            print('красный')
        else:
            print('черный')
    if 19 <= x <= 28:
        if x % 2 == 0:
            print('черный')
        else:
            print('красный')
    if 29 <= x <= 36:
        if x % 2 == 0:
            print('красный')
        else:
            print('черный')
elif x == 0:
    print('зеленый')
else:
    print('ошибка ввода')