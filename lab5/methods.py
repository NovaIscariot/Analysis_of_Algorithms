import threading
from math import ceil

def standart_matrix_mult(a, b, c, k1, k2):
    n = len(a[0])
    q = len(b[0])

    for i in range(k1, k2):
        for j in range(q):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]


def classic_vinograd_mult(a, b, c, k1, k2):
    m = len(a)
    n = len(a[0])
    t = n//2+1

    row_fact = [0 for x in range(m)]
    column_fact = [0 for x in range(len(b[0]))]


    for i in range(m):
        row_fact[i] = 0
        for j in range(1, t):
            row_fact[i] = row_fact[i] + a[i][2*j-2] * a[i][2*j-1]

    for i in range(k1, k2):
        column_fact[i] = 0
        for j in range(1, t):
            column_fact[i] = column_fact[i] + b[2*j-2][i] * b[2*j-1][i]

    for i in range(m):
        for j in range(k1, k2):
            c[i][j] = -row_fact[i] - column_fact[j]
            for k in range(1, t):
                c[i][j] = c[i][j] + (a[i][2*k-2]+b[2*k-1][j])*(a[i][2*k-1] + b[2*k-2][j])

    if (n % 2 == 1):
        for i in range(m):
            for j in range(k1, k2):
                c[i][j] = c[i][j] + a[i][n-1]*b[n-1][j]

def parallel(a, b, func, num):
    n = len(a)
    c = [[0 for x in range(n)] for y in range(n)]

    k = n / num
    tmp = k
    pr_tmp = 0
    threads = []

    for i in range(num-1):
        threads.append(threading.Thread(target=func,
                                        args=(a, b, c, int(pr_tmp),int(tmp))))
        tmp+=k
        pr_tmp+=k
        
    threads.append(threading.Thread(target=func,
                                    args=(a, b, c, int(pr_tmp), ceil(tmp))))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    return c
