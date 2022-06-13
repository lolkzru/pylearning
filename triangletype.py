a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 > 0 and a2 > 0 and a3 > 0:
    if a1 == a2 == a3:
        print('Равносторонний')
    elif a1 != a2 and a2 != a3 and a1 != a3:
        print('Разносторонний')
    else:
        print('Равнобедренный')
