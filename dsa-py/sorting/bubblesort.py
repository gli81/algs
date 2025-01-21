# -*- coding: utf-8 -*-

from typing import List

def bubbleSort(lst: "List[int]") -> "None":
    '''
    sort a list of numbers using bubble sort

    Params
    ----------
        lst List[int]: the list to be sorted

    Returns
    ----------
        None: the list is sorted in place
    '''
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == "__main__":
    test1 = [2, 5, 1]
    bubbleSort(test1)
    print(test1)
    test2 = [1]
    bubbleSort(test2)
    print(test2)
    test3 = []
    bubbleSort(test3)
    print(test3)

