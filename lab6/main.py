from random import randint
import threading
import time

def keyf(e):
    return e[1]

def log_sort(log, n):
    res = []
    for i in range(1,n+1):
        tmp = []
        for j in log:
            if int((j[1].split())[0]) == i:
                tmp.append(j)
        tmp.sort

        for j in tmp:
            res.append(j)
    return res
    
def get_log(log1, log2, log3):
    log = []
    for i in log1:
        log.append(i)
    for i in log2:
        log.append(i)
    for i in log3:
        log.append(i)
    log.sort()
    return log

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def plus_random(n):
    return n+randint(1,n*2-1)

def check_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    if check_prime(n):
        return n
    return next_prime(n)

def factorize(n):
    res = []
    if check_prime(n) == True:
        res.append(n)
    else:
        tmp = n
        i = 2
        while tmp >= i:
            if tmp % i == 0:
                res.append(i)
                tmp //= i
            else:
                i = next_prime(i)

    return res

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
fst_q = []
snd_q = []
trd_q = []
fin_q = []

def fst_conv(n):
    global fst_q
    global log1
    global tb
    
    for i in range(n):
        tmp = randint(1,8)
        log1.append([time.perf_counter()-tb, '{} объект был создан первым конвеером'.format(i+1)])
        mutex1.acquire()
        fst_q.append(tmp)
        mutex1.release()
        log1.append([time.perf_counter()-tb, '{} объект помещен в очередь второго конвеера'.format(i+1)])
    mutex1.acquire()
    fst_q.append(-1)
    mutex1.release()
    return

def snd_conv():
    global fst_q
    global snd_q
    global log2
    global tb
    i = 0
    
    while True:
        time.sleep(10**-5)
        if len(fst_q)>0:
            if fst_q[0] == -1:
                mutex2.acquire()
                snd_q.append(-1)
                mutex2.release()
                return
            tmp = 0
            
            mutex1.acquire()
            tmp = fst_q[0]
            fst_q = fst_q[1:]
            mutex1.release()
            log2.append([time.perf_counter()-tb, '{} объект был взят на обработку вторым конвеером'.format(i+1)])
            
            
            tmp = plus_random(factorial(tmp))

            mutex2.acquire()
            snd_q.append(tmp)
            mutex2.release()
            log2.append([time.perf_counter()-tb, '{} объект помещен в очередь третьего конвеера'.format(i+1)])
            i+=1
            

def trd_conv():
    global snd_q
    global trd_q
    global log3
    global tb
    j = 0
    while True:
        time.sleep(10**-5)
        if len(snd_q)>0:
            if snd_q[0] == -1:
                return
            tmp = 0
            
            mutex2.acquire()
            tmp = snd_q[0]
            snd_q = snd_q[1:]
            mutex2.release()
            log3.append([time.perf_counter()-tb,'{} объект был взят на обработку третьим конвеером'.format(j+1)])
            tmp = factorize(tmp)

            mutex3.acquire()
            trd_q.append(tmp)
            mutex3.release()
            log3.append([time.perf_counter()-tb,'{} объект помещен в очередь четвертого конвеера'.format(j+1)])
            j+=1

n = 100
tb = time.perf_counter()
log1 = []
log2 = []
log3 = []
            
t1 = threading.Thread(target=fst_conv, args=(n,))
t2 = threading.Thread(target=snd_conv)
t3 = threading.Thread(target=trd_conv)

t3.start()
t2.start()
t1.start()

t1.join()
t2.join()
t3.join()

choice = 0
print('1. Вывести обычный лог')
print('2. Вывести лог, сортированный по объекту')
print('3. Вывести лог для определенного объекта')

choice =  int(input('Выберите команду: '))
while choice < 1 or choice > 3:
    choice =  int(input('Выберите команду: '))
log = get_log(log1, log2, log3)
f = open('log.txt', 'w')
    
if (choice >1):
    log = log_sort(log, n)
    if choice == 3:
        i = int(input('Выберите объект от 1 до {}: '.format(n)))
        bot = 0
        top = 0
        for k in range(0,len(log)-1):
            if int((log[k][1].split())[0]) == i and int((log[k+1][1].split())[0]) != i:
                top = k
            if int((log[k][1].split())[0]) != i and int((log[k+1][1].split())[0]) == i:
                bot = k+1
        log = log[bot:top+1]
        
        
for i in log:
    f.write('{:.4f} :'.format(i[0])+i[1]+'\n')
f.close()


print(trd_q)
