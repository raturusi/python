
def geterr(my_val, my_type, my_condition):
    if my_val == "":
        return "Пустой ввод. Повторите ввод."
    elif my_type == "float":
        try:
            my_val = float(my_val)
        except ValueError:
            return "Некорректный ввод. Значение д.б действительным числом. Повторите ввод."
    elif my_type == "int":
        try:
            my_val = int(my_val)
        except ValueError:
            return "Некорректный ввод. Значение д.б. целым числом. Повторите ввод."
    if my_condition == ">0" and not my_val >= 0:
        return "Некорректный ввод. Значение д.б положительным. Повторите ввод."
    elif my_condition == "<0" and not my_val < 0:
        return "Некорректный ввод. Значение д.б отрицательным. Повторите ввод."
    return None

def my_func_pow(x ,y):
    for  i  in range(abs(y)-1):
        x *=x
    return 1/x
def my_func_pow1(x ,y):
    return x**y
while True:
    my_x = input("Введите действительное положительное число:")
    err = geterr(my_x, "float", ">0")
    if err != None:
        print(err)
    else:
        break
while True:
    my_y = input("Введите целое отрицательное число:")
    err = geterr(my_y, "int", "<0")
    if err != None:
        print(err)
    else:
        break
print(f'pow({my_x},{my_y}) = {my_func_pow(float(my_x),int(my_y))}')
print(f'{my_x}**{my_y} = {my_func_pow1(float(my_x),int(my_y))}')