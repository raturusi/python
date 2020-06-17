print("Введите список значений, через запятую(минимум три значения).")
while True:
    my_str = input("? ")
    if my_str == "":
        print("Пустой ввод. Повторите ввод.")
    else:
        my_list = my_str.split(",")
        if len(my_list) < 3:
            print("Введено меньше трех значений. Повторите ввод.")
        else:
            break
print(my_list)
for el in range(len(my_list)//2):
    my_list[el*2], my_list[el*2+1] = my_list[el*2+1], my_list[el*2]
print(my_list)