#тестирование
from ACO import *

import time
import numpy as np
import random as rnd
from matplotlib import pyplot as plt
np.seterr(divide='ignore', invalid='ignore')

MAX_DIS = 10  
MIN_DIS = 1  


def make_d(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            t = rnd.randint(MIN_DIS, MAX_DIS)
            m[i][j], m[j][i] = t, t
    return m

d = make_d(20)
#print(d)
print()


res = []
q_1 = []

time_start = time.perf_counter()
aco(m, 1, d, t_max, 0, 0, 0.8, 1)
time_end = time.perf_counter()
min_v = time_end - time_start

for i in np.arange(0, 2, 0.1):
    for j in np.arange(0, 2, 0.1):
        flag = 0
        time_start = time.perf_counter()
        aco(m, 1, d, t_max, i, j, 0.8, 1)
        time_end = time.perf_counter()

        v = time_end - time_start
        if  v < min_v:
            flag = 1
            min_v = v
        
        q_1.append(time_end - time_start)
        res.append(i+j)
        print(" {0:.2}      {1:.2}        {2:.4}".format(i, j, time_end - time_start), end = " ")
        if flag:
            print("+")
        else:
            print()
        

"""plt.title("time for alpha and betha")
plt.grid(True)
plt.plot(res, q_1)

plt.xlabel('value of alpha and betha')
plt.ylabel('time')
plt.show() 
        
"""
"""
#проверка влияния параметра Q
q_res = []

q = 0
q_1 = []
q_2 = []
q_3 = []
q_4 = []
q_5 = []
while (q < 50):
    time_start = time.perf_counter()
    aco(m, 0, d, t_max, 1, 1, p, q)
    q_res.append(q)
    time_end = time.perf_counter()
    q_1.append(time_end - time_start)

    time_start = time.perf_counter()
    aco(m, 0, d, t_max, 1, 1, p, q)
    time_end = time.perf_counter()
    q_2.append(time_end - time_start)

    time_start = time.perf_counter()
    aco(m, 0, d, t_max, 1, 1, p, q)
    time_end = time.perf_counter()
    q_3.append(time_end - time_start)

    time_start = time.perf_counter()
    aco(m, 0, d, t_max, 1, 1, p, q)
    time_end = time.perf_counter()
    q_4.append(time_end - time_start)

    time_start = time.perf_counter()
    aco(m, 0, d, t_max, 1, 1, p, q)
    time_end = time.perf_counter()
    q_5.append(time_end - time_start)
    
    q += 1


plt.title("time for q")
plt.grid(True)
plt.plot(q_res, q_1)
plt.plot(q_res, q_2)
plt.plot(q_res, q_3)
plt.plot(q_res, q_4)
plt.plot(q_res, q_5)

plt.xlabel('value of Q')
plt.ylabel('time')
plt.show()
    
"""
"""
time_arr = []
time_arr2 = []
time_arr3 = []
res = []
alf = []

#проверка влияния параметров альфа и бета
alpha = 0
while (alpha < 5):
    alf.append(alpha)
    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, alpha, 0, p, 1))
    time_end = time.perf_counter()
    time_arr.append(time_end - time_start)
    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, alpha, 0, p, 1))
    time_end = time.perf_counter()
    time_arr2.append(time_end - time_start)
    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, alpha, 0, p, 1))
    time_end = time.perf_counter()
    time_arr3.append(time_end - time_start)
    alpha += 0.5
    


plt.title("time by alpha")
plt.grid(True)
plt.plot(alf, time_arr)
plt.plot(alf, time_arr2)
plt.plot(alf, time_arr3)
plt.show()

"""

"""
time_arr = []
time_arr2 = []
time_arr3 = []
res = []
beth = []

#проверка влияния параметров альфа и бета
betha = 0
while (betha < 5):
    beth.append(betha)
    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, 0, betha, p, 1))
    time_end = time.perf_counter()
    time_arr.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, 0, betha, p, 1))
    time_end = time.perf_counter()
    time_arr2.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, 1, d, t_max, 0, betha, p, 1))
    time_end = time.perf_counter()
    time_arr3.append(time_end - time_start)
    
    betha += 0.5

plt.title("time by betha")
plt.grid(True)
plt.plot(beth, time_arr)
plt.plot(beth, time_arr2)
plt.plot(beth, time_arr3)
plt.show()

"""

"""
time_arr = []
time_arr2 = []
time_arr3 = []
res = []
eth = []

#проверка влияния параметра e
e = 0
while (e < 5):
    eth.append(e)
    time_start = time.perf_counter()
    res.append(aco(m, e, d, t_max, 1, 1, p, 1))
    time_end = time.perf_counter()
    time_arr.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, e, d, t_max, 1, 1, p, 1))
    time_end = time.perf_counter()
    time_arr2.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, e, d, t_max, 1, 1, p, 1))
    time_end = time.perf_counter()
    time_arr3.append(time_end - time_start)
    
    e += 1
    

plt.title("time by e")
plt.grid(True)
plt.plot(eth, time_arr)
plt.plot(eth, time_arr2)
plt.plot(eth, time_arr3)
plt.show()

"""
"""
time_arr = []
time_arr2 = []
time_arr3 = []
res = []
peth = []

#проверка влияния параметра p
pe = 0
while (pe < 1):
    peth.append(pe)
    time_start = time.perf_counter()
    res.append(aco(m, 0, d, t_max, 1, 1, pe, 1))
    time_end = time.perf_counter()
    time_arr.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, 0, d, t_max, 1, 1, pe, 1))
    time_end = time.perf_counter()
    time_arr2.append(time_end - time_start)

    time_start = time.perf_counter()
    res.append(aco(m, 0, d, t_max, 1, 1, pe, 1))
    time_end = time.perf_counter()
    time_arr3.append(time_end - time_start)
    
    pe += 0.1
    

plt.title("time by p")
plt.grid(True)
plt.plot(peth, time_arr)
plt.plot(peth, time_arr2)
plt.plot(peth, time_arr3)
plt.show()
"""

"""
"""
"""plt.title("res by alpha")
plt.grid(True)
plt.plot(alf, res, "#243253")
plt.show()"""



