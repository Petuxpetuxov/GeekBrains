'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''


revenue = int(input('Write revenue: '))
cost = int(input('Write cost :'))
if revenue > cost:
    profitability = revenue - cost
    print(f'Revenue is more than cost.\nProfitability : {profitability}')
else:
    print('Cost is more than revenue')
size = int(input('Write number of employees :'))
print(f"The company's profit per employee: {(profitability / size): .3f}")


