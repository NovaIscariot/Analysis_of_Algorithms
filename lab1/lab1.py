import time
from random import randint

def string_generator(n):
    res = ""

    for i in range(n):
        res += chr(randint(0, 25)+97)
        
    return res

def print_matrix(matrix, a, b):
    print("", end = "      ")
    for x in a:
        print(x, end = "  ")
    print()
    j = -1
    for i in matrix:
        if j > -1:
            print(b[j], end = " ")
        else:
            print(" ", end = " ")
        j+=1
        print(i)

def levenstain(a, b, print_flag):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
        
    matrix = []
    current_row = [x for x in range(n+1)]

    matrix.append(current_row)

    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1, n+1):
            add  = previous_row[j]+1
            delete = current_row[j-1]+1
            change = previous_row[j-1] + (a[j-1] != b[i-1])
            current_row[j] = min(add, delete, change)
        matrix.append(current_row)

    if print_flag != 0:
        print_matrix(matrix,a,b)

    return current_row[n]

def damerau_levenstain(a, b, print_flag):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
        
    matrix = []
    previous_row = [x for x in range(n+1)]
    current_row = [1]+[0]*n

    for i in range(1, n+1):
        add  = previous_row[i]+1
        delete = current_row[i-1]+1
        change = previous_row[i-1] + (a[i-1] != b[0])
        current_row[i] = min(add, delete, change)

    matrix.append(previous_row)
    matrix.append(current_row)

    for i in range(2, m+1):
        preprevious_row, previous_row, current_row = previous_row, current_row, [i]+[0]*n
        for j in range(1, n+1):
            add  = previous_row[j]+1
            delete = current_row[j-1]+1
            change = previous_row[j-1] + (a[j-1] != b[i-1])
            if j == 1:
                current_row[j] = min(add, delete, change)
            else:
                if a[j-2] == b[i-1] and a[j-1] == b[i-2]:
                    current_row[j] = min(preprevious_row[j-2] + 1, add, delete, change)
                else:
                    current_row[j] = min(add, delete, change)
        matrix.append(current_row)

    if print_flag != 0:
        print_matrix(matrix,a,b)
        
    return current_row[n]

def recurr_levenstain(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    return find_eom(n, m, a, b)

def find_eom(i, j, a, b):
    find_eom.count += 1
    if i == 0:
        return j
    elif j == 0:
        return i
    else:
        el = min(find_eom(i-1, j, a, b)+1, find_eom(i, j-1, a, b)+1,
                           find_eom(i-1, j-1, a, b)+ (a[i-1] != b[j-1]))
    return el

find_eom.count = 0
while (True):
    print()
    print("Выберите пункт меню: ")
    print("1 -- Ручной ввод теста")
    print("2 -- Ручной ввод теста с выводом матриц")
    print("3 -- Замер времени на строках одинаковой длины")
    print("4 -- Замер времени на строках разной длины")
    print("5 -- Подсчет вызовов рекурсивного алгоритма")
    print("0 -- Выход")

    choice = input()
    print()

    if choice == '1':
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        
        print('\nРасстояние Левенштейна: {0}'.format(levenstain(str1, str2, 0)))
        print('Расстояние Дамерау-Левенштейна: {0}'.format(damerau_levenstain(str1, str2, 0)))
        print('Расстояние Левенштейна (Рекурсивный алгоритм): {0}'.format(recurr_levenstain(str1, str2)))
    elif choice == '2':
        str1 = input("Введите первую строку: ")
        str2 = input("Введите вторую строку: ")
        
        print('Расстояние Левенштейна: {0}\n'.format(levenstain(str1, str2, 1)))
        print('Расстояние Дамерау-Левенштейна: {0}\n'.format(damerau_levenstain(str1, str2, 1)))
        print('Расстояние Левенштейна (Рекурсивный алгоритм): {0}'.format(recurr_levenstain(str1, str2)))
    elif choice == '3' or choice == '4':
        if choice == '3':
            n = int(input("Введите число символов в строке: "))
            m = n
        else:
            n = int(input("Введите число символов в первой строке: "))
            m = int(input("Введите число символов во второй строке: "))
        time_levenstain = 0
        time_damerau_levenstain = 0
        time_recurr_levenstain = 0
        for i in range(100):
            str1 = string_generator(n)
            str2 = string_generator(m)
            
            tmp_time1 = time.perf_counter()
            levenstain(str1, str2, 0)
            tmp_time2 = time.perf_counter()
            damerau_levenstain(str1, str2, 0)
            tmp_time3 = time.perf_counter()
            recurr_levenstain(str1, str2)
            tmp_time4 = time.perf_counter()

            time_levenstain += (tmp_time2 - tmp_time1)
            time_damerau_levenstain += (tmp_time3 - tmp_time2)
            time_recurr_levenstain += (tmp_time4 - tmp_time3)
        time_levenstain /= 100
        time_damerau_levenstain /= 100
        time_recurr_levenstain /= 100
        print('Время работы алгоритма Левенштейна: {0}'.format(time_levenstain))
        print('Время работы алгоритма Дамерау-Левенштейна: {0}'.format(time_damerau_levenstain))
        print('Время работы рекурсивного алгоритма Левенштейна: {0}'.format(time_recurr_levenstain))
    elif choice == '5':
        find_eom.count = 0
        n = int(input("Введите число символов в первой строке: "))
        m = int(input("Введите число символов во второй строке: "))
        str1 = string_generator(n)
        str2 = string_generator(m)
        recurr_levenstain(str1, str2)
        print('Количество вызовов: {0}'.format(find_eom.count))
    elif choice == '0':
        break
    else:
        print("Нет такого пункта меню")
    
