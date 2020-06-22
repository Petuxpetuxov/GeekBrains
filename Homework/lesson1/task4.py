'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''


while True:
    number = input('Write number: ')
    if number.isdigit() and int(number) > 0:
        number = int(number)
        break
    else:
         print("Write positive number")
result = 0
while number and result != 9:
    step = number % 10
    if step > result:
        result = step
    number //= 10
print(result)






