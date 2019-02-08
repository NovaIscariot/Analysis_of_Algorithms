def levenstain(a, b, print_flag):  
    n, m = len(a), len(b)                                  #1
    if n > m:                                              #2
        a, b = b, a                                        #3
        n, m = m, n                                        #4
        
    matrix = []                                            #5
    current_row = [x for x in range(n+1)]                  #6

    matrix.append(current_row)                             #7

    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n #8
        for j in range(1, n+1):
            add  = previous_row[j]+1                       #9
            delete = current_row[j-1]+1                    #10
            change = previous_row[j-1] + (a[j-1] != b[i-1])#11
            current_row[j] = min(add, delete, change)      #12
        matrix.append(current_row)                         #13

    if print_flag != 0:                                    
        print_matrix(matrix,a,b)

    return current_row[n]
