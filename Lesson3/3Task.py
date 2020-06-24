def my_summax(num1, num2, num3):
    f_list = [num1, num2, num3]
    f_list.remove(min(f_list))
    return f_list[0] + f_list[1]

while True:
    my_i = input("Введите три  числа,  через пробел:")
    if my_i == "":
        print("Пустой ввод. Повторите ввод.")
    else:
        my_list = my_i.split(" ")
    if len(my_list) < 3:
        print("Некорректный ввод. Требуется  три  числа, через пробел. Повторите ввод.")
    else:
        try:
            result = my_summax(float(my_list[0]), float(my_list[1]), float(my_list[2]))
            print(f'Максимальная сумма из двух чисел = {result}')
            break
        except ValueError:
            print("Некорректный ввод. Значения д.б числами. Повторите ввод.")



