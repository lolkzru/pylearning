a = input()
b = input()
if a == 'красный' or a == 'синий' or a == 'желтый':
    if b == 'красный' or b == 'синий' or b == 'желтый':
        if a == 'красный' and b == 'красный':
            print('красный')
        elif a == 'синий' and b == 'синий':
            print('синий')
        elif a == 'желтый' and b == 'желтый':
            print('желтый')
        elif a == 'красный' and b == 'синий':
            print('фиолетовый')
        elif a == 'синий' and b == 'красный':
            print('фиолетовый')
        elif a == 'красный' and b == 'желтый':
            print('оранжевый')
        elif a == 'желтый' and b == 'красный':
            print('оранжевый')
        elif a == 'синий' and b == 'желтый':
            print('зеленый')
        elif a == 'желтый' and b == 'синий':
            print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')