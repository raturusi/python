while True:
    s = input("Введите целое положительное число:")
    while True:
        if s == None or s == "":
            print("Пустой ввод. Повторите ввод.")
        elif int(s) < 0:
            print("Задано отрицательное значение. Повторите ввод.")
        else:
            break
        s = input("Введите число:")
    s = int(s)
    s1 = int(str(s) + str(s))
    s2 = int(str(s) + str(s) + str(s))
    sm = s + s1 + s2
    print(f'n + nn + nnn = {sm} ')
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break
