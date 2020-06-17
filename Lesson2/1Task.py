my_str = "lesson2"
my_list = list(my_str)
my_list.insert(0, 5)
my_list.append(my_str)
my_list.extend((5.5, 10, "2020", "GeekBrains"))
print(my_list)
my_list.pop(4)
print(my_list)
for el in my_str:
    if my_list.count(el) != 0:
        my_list.remove(el)
    else:
        print(f'{el} - не найден')
print(my_list)
for el in range(len(my_list)):
   print(f'{my_list[el]} = {type(my_list[el])}')
print("А теперь все наборот")
my_list.reverse()
print(my_list)
for el in my_list:
   print(f'{el} = {type(el)}')
my_list.append(None)
my_list.append(1 == 2)
my_list.append(6+7j)
my_list.append([1, 2.0])
my_list.append(("June", "Jule"))
my_list.append({"August", "September"})
my_list.append({'key_1': 'val_1', 'key_2': 'val_2'})
my_list.append(type(Exception));
my_list.append(Exception);
print(my_list)
for el in my_list:
   if type(el) == str:
       print(f'{el} - Строка! {type(el)}')
   elif type(el) == int:
       print(f'{el} - Целое число! {type(el)}')
   elif type(el) == float:
       print(f'{el} - Число с плаваяющей точкой! {type(el)}')
   elif type(el) == bool:
       print(f'{el} - Булевый! {type(el)}')
   elif type(el) == complex:
       print(f'{el} - Комплексный! {type(el)}')
   elif type(el) == list:
       print(f'{el} - Список! {type(el)}')
   elif type(el) == tuple:
       print(f'{el} - Кортеж! {type(el)}')
   elif type(el) == set:
       print(f'{el} - Массив! {type(el)}')
   elif type(el) == dict:
       print(f'{el} - Словарь! {type(el)}')
   elif type(el) == tuple:
       print(f'{el} - Кортеж! {type(el)}')
   elif el == Exception:
       print(f'{el} - Исключение! type{el}')
   elif type(el) == type:
       print(f'{el} - Тип данных! type{el}')
   else:
       print(f'{el} - Null! {type(el)}')
