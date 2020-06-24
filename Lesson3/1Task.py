def divide(divident, divider):
    try:
        result = divident / divider
        return result
    except ZeroDivisionError:
        print("Делить на ноль нельзя")

while True:
    my_i = input("Введите два целых числа, делимое и делитель, через пробел:")
    if my_i == "":
        print("Пустой ввод. Повторите ввод.")
    else:
        my_list = my_i.split(" ")
    if len(my_list) < 2:
        print("Некорректный ввод. Повторите ввод.")
    elif not (my_list[0] if my_list[0][0:1] != '-' else my_list[0][1:len(my_list[0])]).isdigit() or \
            not (my_list[1] if my_list[1][0:1] != '-' else my_list[1][1:len(my_list[1])]).isdigit():
        print(f'Некорректный ввод. {my_list[0]+" - не число." if not (my_list[0] if my_list[0][0:1] != "-" else my_list[0][1:len(my_list[0])]).isdigit() else ""} '
              f'{my_list[1]+" - не число." if not (my_list[1] if my_list[1][0:1] != "-" else my_list[1][1:len(my_list[1])]).isdigit() else ""} Повторите ввод.')
    else:
        break
result = divide(float(my_list[0]), float(my_list[1]))
if result != None:
    print(f'{my_list[0]}/{my_list[1]} = {result}')