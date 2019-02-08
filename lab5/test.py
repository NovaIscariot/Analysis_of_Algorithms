from time import perf_counter_ns
from methods import standart_matrix_mult, classic_vinograd_mult, parallel
from random import randint

def smm(a, b):
    m = len(a)
    n = len(a[0])
    q = len(b[0])
    c = [[0 for x in range(q)] for y in range(m)]

    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c


def random_matrix_generator(n):
    return [[randint(0,10) for x in range(n)] for y in range(n)]


x = [2**i for i in range(5)]
for length in range(101, 802, 100):
    print('N = {:d}'.format(length))
    a = random_matrix_generator(length)
    b = random_matrix_generator(length)
    for i in x:
        print("   Количество потоков: {:d}".format(i))
        psmm = 0
        pcvm = 0
        n = 10
        for j in range(n):
            tb = perf_counter_ns()
            parallel(a,b,standart_matrix_mult,i)
            psmm += perf_counter_ns() - tb
            
            tb = perf_counter_ns()
            parallel(a,b,classic_vinograd_mult,i)
            pcvm += perf_counter_ns() - tb

        print('   Классический алгоритм умножения матриц: {0}'.format(psmm/10**9/n))
        print('   Классический алгоритм винограда:        {0}'.format(pcvm/10**9/n))
        print('   ------------------------')

