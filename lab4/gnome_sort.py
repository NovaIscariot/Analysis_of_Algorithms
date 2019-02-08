def gnome_sort(a):
    i = 0
    while i < len(a)-1:
        if (a[i] > a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            if i > 1:
                i -= 2
        i+=1

    return a
