print("Введите список слов, через пробел(минимум два слова).")
while True:
    my_str = input("? ")
    if my_str == "":
        print("Пустой ввод. Повторите ввод.")
    else:
        my_list = my_str.split(" ")
        if len(my_list) < 2:
            print("Введено меньше двух слов. Повторите ввод.")
        else:
            break
print(my_list)
for el in enumerate(my_list):
    print(f'{el[0]+1} - {el[1][0:10:]}')
