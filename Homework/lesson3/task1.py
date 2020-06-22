"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
a = int(input('Write first number: '))
b = int(input('Write second number: '))
def numbers():
    try:
        a / b
    except ZeroDivisionError:
        print('Делить на 0 нельзя')
    return a / b
print(numbers())





