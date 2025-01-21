# -*- coding: utf-8 -*-

# import time
from typing import List
import random

def quickSort(lst: "List[int]") -> "None":
    '''
    sort a list of numbers using quick sort

    Params
    ----------
        lst List[int]: the list to be sorted

    Returns
    ----------
        None: the list is sorted in place
    '''
    quickSortHelper3(lst, 0, len(lst))

def quickSortHelper1(lst: "List[int]", start: "int", end: "int") -> "None":
    '''
    quick sort helper function that
    having the starting element as pivot

    Params
    ----------
        lst List[int]: the list part of which to be sorted
        start int: the starting index of the subarray be sorted
        end int: the ending index of the subarray to be sorted

    Returns
    ----------
        None: the list is sorted in place
    '''
    ## set pivot
    r = end - 1
    if start < r:
        p = start
        l = start + 1
        while True:
            while l <= r and lst[l] <= lst[p]:
                l += 1
            while r >= l and lst[r] >= lst[p]:
                r -= 1
            ## two numbers found
            ## if l and r not met yet, swap
            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
            else:
                ## if met, end loop, put pivot to r
                break
        lst[r], lst[p] = lst[p], lst[r]
        ## sort two subarray
        quickSortHelper1(lst, start, r)
        quickSortHelper1(lst, r + 1, end)

def quickSortHelper2(lst: "List[int]", start: "int", end: "int") -> "None":
    '''
    quick sort helper function that
    having the middle element as pivot

    Params
    ----------
        lst List[int]: the list part of which to be sorted
        start int: the starting index of the subarray be sorted
        end int: the ending index of the subarray to be sorted

    Returns
    ----------
        None: the list is sorted in place
    '''
    ## set pivot
    r = end - 1
    if start < r:
        p = (end - start) // 2 + start
        lst[p], lst[start] = lst[start], lst[p]
        l = start + 1
        while True:
            while l <= r and lst[l] <= lst[start]:
                l += 1
            while r >= l and lst[r] > lst[start]:
                r -= 1
            ## two numbers found
            ## if l and r not met yet, swap
            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
            else:
                ## if met, end loop, put pivot to r
                break
        lst[r], lst[start] = lst[start], lst[r]
        ## sort two subarray
        quickSortHelper2(lst, start, r)
        quickSortHelper2(lst, r + 1, end)

def quickSortHelper3(lst: "List[int]", start: "int", end: "int") -> "None":
    '''
    quick sort helper function that
    having random element as pivot

    Params
    ----------
        lst List[int]: the list part of which to be sorted
        start int: the starting index of the subarray be sorted
        end int: the ending index of the subarray to be sorted

    Returns
    ----------
        None: the list is sorted in place
    '''
    ## set pivot
    r = end - 1
    if start < r:
        p = random.randint(start, r)
        lst[p], lst[start] = lst[start], lst[p]
        l = start + 1
        while True:
            while l <= r and lst[l] <= lst[start]:
                l += 1
            while r >= l and lst[r] > lst[start]:
                r -= 1
            ## two numbers found
            ## if l and r not met yet, swap
            if l < r:
                lst[l], lst[r] = lst[r], lst[l]
            else:
                ## if met, end loop, put pivot to r
                break
        lst[r], lst[start] = lst[start], lst[r]
        ## sort two subarray
        quickSortHelper3(lst, start, r)
        quickSortHelper3(lst, r + 1, end)

if __name__ == "__main__":
    test1 = [2, 5, 1, 3]
    quickSort(test1)
    print(test1)
    test2 = [2, 5, 1]
    quickSort(test2)
    print(test2)
    test3 = [1]
    quickSort(test3)
    print(test3)
    test4 = []
    quickSort(test4)
    print(test4)
    # ## test array access vs. append
    # test_ = [2, 7, 2, 9, 4, 8, 3 ,67, 7845, 23, 65, 789, 234, 58,12, 976]
    # test = []
    # for num in test_:
    #     test.append(num)
    # for num in test_:
    #     test.append(num + 25)
