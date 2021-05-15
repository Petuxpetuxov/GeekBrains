"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if a > b:
    if b < c:
        print(c)
    else:
        print(b)
else:
    if a > c:
        print(a)
    elif a < c:
        if b < c:
            print(b)
        else:
            print(c)
