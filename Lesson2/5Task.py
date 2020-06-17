my_list = [7, 5, 3, 3, 2]
while True:
    while True:
        m = input("Введите целое число от 0 до 10 ")
        if m == "":
            print("Пустой ввод. Повторите ввод.")
        elif m not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
            print("Некорректный ввод. Повторите ввод.")
        else:
            break
    for el in range(len(my_list)):
        if my_list[len(my_list) - el - 1] >= int(m):
            if el == 0:
                my_list.append(int(m))
                break
            else:
                my_list.insert(len(my_list) - el, int(m))
                break
        elif el == len(my_list)-1:
            my_list.insert(len(my_list) - el - 1, int(m))
    print(my_list)
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break
