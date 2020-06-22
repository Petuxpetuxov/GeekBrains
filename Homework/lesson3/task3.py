"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
a = int(input('Write first number: '))
b = int(input('Write second number: '))
c = int(input('Write third number: '))
def my_func():
    if a > b > c:
        max_1 = a
        max_2 = b
    elif a > b < c:
        max_1 = a
        max_2 = c
    elif a < b < c:
        max_1 = c
        max_2 = b
    elif a < b > c:
        max_1 = b
        if a < c:
            max_2 = c
        else:
            max_2 = a
    return max_1 + max_2
print(my_func())