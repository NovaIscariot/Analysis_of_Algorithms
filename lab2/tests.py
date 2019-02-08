from time import perf_counter_ns, process_time_ns
from random import randint
from lab2 import *

def random_matrix_generator(n):
    return [[randint(0,100) for x in range(n)] for y in range(n)]


'''print("Тест на четных размерностях: ")
for x in range(100, 901, 100):
    print('N = {:d}'.format(x))
    n = 10
    time_smm = 0
    time_cvm = 0
    time_ovm = 0
    for y in range(n):
        a = random_matrix_generator(x)
        b = random_matrix_generator(x)
        
        time_b = process_time_ns()
        standart_matrix_mult(a,b)
        time_smm += (process_time_ns() - time_b)
        
        time_b = process_time_ns()
        classic_vinograd_mult(a,b)
        time_cvm += (process_time_ns() - time_b)
        
        time_b = process_time_ns()
        optimized_vinograd_mult(a,b)
        time_ovm += (process_time_ns() - time_b)
        
    time_smm/=(n*10**9)
    time_cvm/=(n*10**9)
    time_ovm/=(n*10**9)
    print('Классический алгоритм умножения матриц: {0}'.format(time_smm))
    print('Классический алгоритм винограда:        {0}'.format(time_cvm))
    print('Оптимизированный алгоритм винограда:    {0}'.format(time_ovm))
    print('--------------------------')
'''

print("\n\nТест на нечетных размерностях: ")
for x in range(101, 902, 100):
    print('N = {:d}'.format(x))
    n = 10
    time_smm = 0
    time_cvm = 0
    time_ovm = 0
    for y in range(n):
        a = random_matrix_generator(x)
        b = random_matrix_generator(x)
        
        time_b = process_time_ns()
        standart_matrix_mult(a,b)
        time_smm += (process_time_ns() - time_b)
        
        time_b = process_time_ns()
        classic_vinograd_mult(a,b)
        time_cvm += (process_time_ns() - time_b)
        
        time_b = process_time_ns()
        optimized_vinograd_mult(a,b)
        time_ovm += (process_time_ns() - time_b)
        
    time_smm/=(n*10**9)
    time_cvm/=(n*10**9)
    time_ovm/=(n*10**9)
    print('Классический алгоритм умножения матриц: {0}'.format(time_smm))
    print('Классический алгоритм винограда:        {0}'.format(time_cvm))
    print('Оптимизированный алгоритм винограда:    {0}'.format(time_ovm))
    print('--------------------------')

