"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
name = str(input('Whats your name: '))
birthdayYear = int(input('When were you born(year): '))
city = str(input('Where are you live(town): '))
phoneNumber = int(input('Whats your phone number: '))
def info(name, birthdayYear, city, phoneNumber):
    return name, birthdayYear, city, phoneNumber
print(f"Your name: {name}.You was born in {birthdayYear}.You live in {city}.Your phone number: {phoneNumber}")