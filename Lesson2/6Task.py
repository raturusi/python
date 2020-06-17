my_list = list()

print("Введите позицию товара:")
n = 0
while True:
    name = input("Название товара: ")
    my_dict = dict(название=name)
    cost = input("Цена: ")
    my_dict.update(dict(цена=cost))
    qnt = input("Кол-во товара: ")
    my_dict.update(dict(количество=qnt))
    unit = input("Единица измерения: ")
    my_dict.update(dict(ед=unit))
    n += 1
    my_list.append((n, my_dict))
    y = input('Продолжить ввод товара y/n? ')
    if y == 'n':
        break
print(my_list)

list_name = list()
list_cost = list()
list_qnt = list()
list_unit = list()

for el in my_list:
    for key, value in el[1].items():
        if key == "название":
            list_name.append(value)
        elif key == "цена":
            list_cost.append(value)
        elif key == "количество":
            list_qnt.append(value)
        elif key == "ед":
            list_unit.append(value)

my_dict = {"название": list_name,"цена": list_cost, "количество": list_qnt, "ед": list_unit }
for key, value in my_dict.items():
    print(f'{key} - {value}')
