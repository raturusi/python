import datetime
firstname = "Иван"
secondname = "Иванов"
bithday = "01.01.2000"
age = (datetime.date.today()-datetime.datetime.strptime(bithday,"%d.%m.%Y").date()).days//365
print(age)
print(f'{"Имя":<20}{"Фамилия":<20}{"День рождения":<20}{"Возраст":<20}')
print(f'{firstname:<20}{secondname:<20}{bithday:<20}{str(age):<20}')

firstname = input('Ваше имя? ')
secondname = input('Фамилия? ')
bithday = input('День рождения? ')
age = (datetime.date.today()-datetime.datetime.strptime(bithday,"%d.%m.%Y").date()).days//365
print(f'{firstname:<20}{secondname:<20}{bithday:<20}{str(age):<20}')

