while True:
    s = input("Введите время в секундах:")
    while True:
        if s == None or s == "":
            print("Пустой ввод. Повторите ввод.")
        elif int(s) < 0:
            print("Задано отрицательное значение. Повторите ввод.")
        else:
            break
        s = input("Введите время в секундах:")
    s = int(s)
    h = s//3600
    m = s//60 - h * 60
    ss = s - h * 3600 - m * 60
    print(f'{h:02d}:{m:02d}:{ss:02d}')
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break
