'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''


firstDay = int(input('How many km did you run on the first day:'))
lastDay = int(input('How many km do you want to run :'))
distance = firstDay
day = 0
while distance <= lastDay:
    day = day + 1
    distance = distance * 1.1
    print(f"On the {day} day you have ran : {distance: .2f} km")


