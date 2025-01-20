# -*- coding: utf-8 -*-

import time
from typing import List

def mergeSort(lst: "List[int]") -> "List[int]":
    n = len(lst)
    if n < 2: return lst
    mid = n // 2
    l = lst[:mid]
    r = lst[mid:]
    l = mergeSort(l)
    r = mergeSort(r)
    ans = [0] * n
    j = k = 0
    llen = len(l)
    rlen = len(r)
    for i in range(n):
        if j >= llen:
            ## nothing left in l
            ans[i] = r[k]
            k += 1
        elif k >= rlen:
            ## nothing left in r
            ans[i] = l[j]
            j += 1
        elif l[j] > r[k]:
            ans[i] = r[k]
            k += 1
        else:
            ans[i] = l[j]
            j += 1
    return ans


def mergeSort2(lst: "List[int]") -> "List[int]":
    n = len(lst)
    if n < 2: return lst
    mid = n // 2
    l = lst[:mid]
    r = lst[mid:]
    l = mergeSort(l)
    r = mergeSort(r)
    ans = []
    j = k = 0
    llen = len(l)
    rlen = len(r)
    for i in range(n):
        if j >= llen:
            ## nothing left in l
            ans.append(r[k])
            k += 1
        elif k >= rlen:
            ## nothing left in r
            ans.append(l[j])
            j += 1
        elif l[j] > r[k]:
            ans.append(r[k])
            k += 1
        else:
            ans.append(l[j])
            j += 1
    return ans

if __name__ == "__main__":
    test1 = [2, 5, 1, 3]
    print(mergeSort(test1))
    test2 = [2, 5, 1]
    print(mergeSort(test2))
    test3 = [1]
    print(mergeSort(test3))
    test4 = []
    print(mergeSort(test4))
    ## test array access vs. append
    test_ = [2, 7, 2, 9, 4, 8, 3 ,67, 7845, 23, 65, 789, 234, 58,12, 976]
    test = []
    for num in test_:
        test.append(num)
    for num in test_:
        test.append(num + 25)
    start = time.time()
    for i in range(500000):
        mergeSort(test)
    end = time.time()
    print(f"Array access: {end-start:.4f}")
    start = time.time()
    for i in range(500000):
        mergeSort2(test)
    end = time.time()
    print(f"Append: {end-start:.4f}")
