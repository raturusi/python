
my_lambda_sum = lambda p1, p2: p1 + p2
my_sum = 0
while True:
    my_val = 0
    my_list = input("Введите строку чисел для вычисления суммы,  через пробел (q для выхода из программы):").split()
    for i in (range(len(my_list)) if my_list.count('q') == 0 else range(my_list.index('q'))):
        try:
            my_val = my_lambda_sum(my_val, float(my_list[i]))
        except ValueError:
            print(f'Ошибка ввода значения {my_list[i]}')
    print(f'{my_sum} + sum{my_list} = {my_sum + my_val}')
    my_sum += my_val
    if my_list.count('q') != 0:
        print('Выход')
        break

