def my_person(sname, fname, bythday, email, city, phone):
     print(f'First name: {fname}, Second name: {sname}, Bythday: {bythday}, Residence: {city}, Email: {email}, Phone number: {phone}')
     """ Проверяем """
     for el in my_dict.keys():
         print(f'{el}: {my_dict[el]+("," if el != "Phone number" else "")} ', end='')

my_dict = {"First name": "", "Second name": "", "Bythday": "", "Residence": "", "Email": "", "Phone number": ""}
print('Please, input:')
for el in my_dict.keys():
    my_dict[el] = input(f'{el}? ')
print(my_dict)
my_person(fname=my_dict["First name"], sname=my_dict["Second name"], bythday=my_dict["Bythday"], city=my_dict["Residence"], email=my_dict["Email"], phone=my_dict["Phone number"])

