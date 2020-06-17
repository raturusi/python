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
    m=0
    while True:
        m1 = s % 10
        if m1 > m:
            m = m1
        s = s // 10
        print(f'm = {m}; s = {s}')
        if s == 0:
            break
    print(f'Максимальное значение из введенной последовательности = {m} ')
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break
