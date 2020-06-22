'''1 минута = 60 секунд
   1 час = 60 минут = 3600 секунд
   Пользователь вводит время в секундах.
   Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
   Используйте форматирование строк.
'''


userNumber = int(input('Write number of seconds: '))
hours = userNumber // 3600
minutes = (userNumber % 3600) // 60
seconds = (userNumber % 3600) % 60

print(f" In {userNumber} seconds there are {hours} hours, {minutes} minutes, {seconds} seconds")
