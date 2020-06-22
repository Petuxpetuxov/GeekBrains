"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def numbers(*args):
    result = 0
    exit = False
    for itm in args:
        try:
            result += float(itm)
        except ValueError:
            if itm == 'q':
                exit = not exit
                break
    return result, exit
numbers_sum = 0
user_exit = False
while not user_exit:
    user_input = input('Введите числа через пробел :').split(' ')
    result_sum, user_exit = numbers(*user_input)
    numbers_sum += result_sum
    print(f'Сумма равна {numbers_sum}')


