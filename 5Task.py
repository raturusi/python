while True:
    s = input("Введите выручку:")
    i = input("Введите издержки:")
    while True:
        if i == "" or s == "":
            print("Пустой ввод. Повторите ввод.")
        elif float(i) < 0 or float(s) < 0:
            print("Задано отрицательное значение. Повторите ввод.")
        else:
            break
        s = input("Введите выручку:")
        i = input("Введите издержки:")
    r = float(s) - float(i)
    if r >= 0:
        print(f'Вы получили прибыль {r:.2f}, Ваша рентабельность = {r / float(i):.2f}')
        c = input('Количество сотрудников в фирме? ')
        while True:
            if c == "":
                print("Пустой ввод. Повторите ввод.")
            elif int(c) <= 0:
                print("Значение должно быть > 0. Повторите ввод.")
            else:
                break
            c = input('Количество сотрудников в фирме? ')
        print(f'Прибыль на одного сотрудника составляет {r / int(c):.2f}')
    else:
        print(f'Вы получили убыток {r * -1:.2f}')
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break