import time
from random import randint

def string_generator(n):
    res = ""

    for i in range(n):
        res += chr(randint(0, 2)+97)
        
    return res

def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

def kmp(substr,mainstr):
    index = -1
    f = prefix(substr)
    k = 0
    for i in range(len(mainstr)):
        while k > 0 and substr[k] != mainstr[i]:
            k = f[k-1]
        if substr[k] == mainstr[i]:
            k = k + 1
        if k == len(substr):
            index = i - len(substr) + 1
            break
    return index


def shifts(s):
    return {a: len(s[:-1]) - s[:-1].rfind(a)  for a in s[:-1]}

def bm(substr,mainstr):
    ln = len(substr)
    index = ln
    sdict = shifts(substr)
    while index <= len(mainstr):
        if substr == mainstr[index-ln:index]:
            return index-ln
        else:
            if mainstr[index-1] in sdict.keys():
                index += sdict.get(mainstr[index-1])
            else:
                index += ln
    return -1


mstr = string_generator(40)
sstr = string_generator(3)
print(shifts(sstr))
print(mstr)
print(sstr)
print(mstr.find(sstr))
print(kmp(sstr, mstr))
print(bm(sstr, mstr))
