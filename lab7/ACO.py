
import numpy as np
import random as rnd
np.seterr(divide='ignore', invalid='ignore')

#const
m = 5 #количество городов
t_max = 100
dist_min = 1 
dist_max = 10 
p = 0.5 #испарение



def aco(m, e, d, t_max, alpha, beta, p, q):
    nue = 1 / d  
    teta = np.random.sample((m, m))
    T_min = None 
    L_min = None 

    t = 0  

    while t < t_max:
        teta_k = np.zeros((m, m))

        for k in range(m): 
            Tk = [k]
            Lk = 0
            i = k   

            while len(Tk) != m:
                J = [r for r in range(m)]   
                for c in Tk:  
                    J.remove(c)

                P = [0 for alpha in J]

                for j in J:
                    if d[i][j] != 0:  
                        buf = sum((teta[i][l] ** alpha) * (nue[i][l] ** beta) for l in J)
                        P[J.index(j)] = (teta[i][j] ** alpha) * (nue[i][j] ** beta) / buf
                    else:
                        P[J.index(j)] = 0

                Pmax = max(P)
                if Pmax == 0:
                    break

                index = P.index(Pmax) 
                Tk.append(J[index])   
                Lk += d[i][J[index]] 
                i = J.pop(index)  

            if L_min is None or (Lk + d[Tk[0]][Tk[-1]]) < L_min:  
                L_min = Lk + d[Tk[0]][Tk[-1]]                   
                T_min = Tk

            for g in range(len(Tk) - 1):   
                alpha= Tk[g]
                betha = Tk[g + 1]
                teta_k[alpha][betha] += q / Lk

        teta_e = (e * q / L_min) if L_min else 0  
        teta = (1 - p) * teta + teta_k + teta_e    
        t += 1

    return L_min


