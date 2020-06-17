while True:
    a = input("Введите пробег(км) в первый день a = ")
    b = input("Введите требуемый пробег b = ")
    while True:
        if a == "" or b == "":
            print("Пустой ввод. Повторите ввод.")
        elif float(a) < 0 or float(b) < 0:
            print("Задано отрицательное значение. Повторите ввод.")
        elif float(a) >= float(b):
            print("Значение a д.б. < b. Повторите ввод.")
        else:
            break
        a = input("Введите пробег(км) в первый день a = ")
        b = input("Введите требуемый пробег b = ")
    d = 1
    a = float(a)
    while True:
            a += a * 0.1
            d += 1
            print(f'{d}-й день, пробег = {a:.2f}')
            if a >= float(b):
                print(f' Требуемый результат достигнут нв {d}-й день и составляет {a:.2f} км, что >={b} км')
                break
    y = input('Продолжить вычисления y/n? ')
    if y == 'n':
        break
