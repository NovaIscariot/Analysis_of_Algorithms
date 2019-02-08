def barier_sort(a):
    barier = 0                            #1
    for i in range(1, len(a)):            #
        if a[i-1]>a[i]:                   #2
            barier = a[i]                 #3
            j = i-1                       #4
            while a[j]>barier and j>-1:   #
                a[j+1] = a[j]             #5
                j -= 1                    #6
            a[j+1] = barier               #7
            
    return a

source = [2, 4, 3, 1]

barier_sort(source)
