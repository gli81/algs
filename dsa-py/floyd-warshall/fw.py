# -*- coding: utf-8 -*-

'''
implementation of Floyd Warshall algorithm

Floyd Warshall algorithm finds the shortest path between any 2 vertices

@author: Gavin Li
@email: liguangzheng998@hotmail.com
@created: 08212024
'''

from typing import List
import time

INF: "int" = 10**18

def fw_recur_helper_1(
    adjMat: "List[List[int]]",
    i: "int",
    j: "int",
    k: "List[int]"
) -> "int":
    '''
    floyd warshall recursion helper function 1
    finds shortest path between i th vertex and j th vertex

    Params
    ----------
        adjMat List[List[int]]: adjacency matrix
        i int: calculate shortest path from the i th vertex in graph
        j int: calculate shortest path to the j th vertex in graph
        k List[int]: list of indecies of vertcies in graph

    Returns
    ----------
        int: the shorter distance between
            going through the k[-1] th vertex from i th to j th
            and going directly from i th to j th
    '''
    ## base call base call, no available vertex between i and j
    if not k:
        ## not neighbors are represented with INF in adjMat
        return adjMat[i][j]
    ## recursive calls
    ## use it, i => k[-1] => j
    thru = k.pop()
    use_it = fw_recur_helper_1(
        adjMat, i, thru, k
    ) + fw_recur_helper_1(
        adjMat, thru, j, k
    )
    ## lose it, i => j, potentially through other points in k
    lose_it = fw_recur_helper_1(adjMat, i, j, k)
    k.append(thru)
    return min(use_it, lose_it)

def fw_recur_helper_2(
    adjMat: "List[List[int]]",
    i: "int",
    j: "int",
    k: "int"
):
    '''
    floyd warshall recursion helper function 2
    since exploring whether to use or lose
    the highest order vertex every time, 
    change k from a list of nodes 
    to the current highest order vertex

    Params
    ----------
        adjMat List[List[int]]: adjacent matrix
        i int: calculate shortest path from the i th vertex in graph
        j int: calculate shortest path to the j th vertex in graph
        k int: index of current highest order vertex being explored

    Returns
    ----------
        int:  the shorter distance between
            going through the k th vertex from the i th to the j th
            and going directly from i th to j th
    '''
    ## base call, no available vertex between i and j
    if k < 0:
        return adjMat[i][j]
    ## recursive calls
    use_it = fw_recur_helper_2(
        adjMat, i, k, k - 1
    ) + fw_recur_helper_2(
        adjMat, k, j, k - 1
    )
    ## lose it, i => j, potentially through other points in k
    lose_it = fw_recur_helper_2(adjMat, i, j, k - 1)
    return min(use_it, lose_it)

def fw_recur(
    adjMat: "List[List[int]]",
    use_list: "bool"=False
) -> "List[List[int]]":
    '''
    floyd warshall with recursion

    Params
    ----------
        adjMat List[List[int]]: adjacency matrix
        use_list bool: flag for use helper function that 
            uses a list of vertices

    Returns
    ----------
        List[List[int]]: a matrix noting shortest path
            between any two vertices
    '''
    ## initialize result matrix
    ans = [
        [0 for _ in range(len(adjMat[0]))] for _ in range(len(adjMat))
    ]
    ## for each pair of src and dest, find shortest path
    for i in range(len(adjMat)):
        for j in range(len(adjMat[0])):
            if use_list:
                ans[i][j] = fw_recur_helper_1(
                    adjMat, i, j, [n for n in range(len(adjMat))]
                )
            else:
                ans[i][j] = fw_recur_helper_2(
                    adjMat, i, j, len(adjMat) - 1
                )
    return ans

'''
TODO recursion with memoization
'''

def fw_dp(adjMat: "List[List[int]]") -> "List[List[List[int]]]":
    '''
    floyd warshall with dynamic programming

    Params
    ----------
        adjMat List[List[int]]: adjacency matrix

    Returns
    ----------
        List[List[List[int]]] : 3D dp table
            first dimension represents decision
                whether going thru the vertex
            second dimension represents src
            third dimension represents dest
    '''
    n = len(adjMat)
    dp = [
        [
            [
                INF for _ in range(n)
            ] for _ in range(n)
        ] for _ in range(n + 1)
        ## becasue base case is no available vertex
        ## in total n + 1 possible cases for going thru vertex
    ]
    ## base case: no available vertex to go through,
    ## i and j are neighbor
    ## the first plane in dp table represents no available vertex
    ## (k = -1 or k = [] in recursion)
    for i in range(n):
        for j in range(n):
            dp[0][i][j] = adjMat[i][j]
    ## fill in the rest
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                ## use the current k or lose it
                dp[k][i][j] = min(
                    dp[k - 1][i][k - 1] + dp[k - 1][k - 1][j], ## use it
                    ## becasue base case is no available vertex
                    ## in total n + 1 possible cases 
                    ## for going thru vertex
                    ## so index k = 0 represents (no more vertex)
                    ## index k = 1 represents going thru the 0th vertex
                    dp[k - 1][i][j] ## lose it
                )
    # ## visualization code
    # print('=' * 20)
    # for plane in dp:
    #     for row in plane:
    #         print(row)
    #     print('-' * 20)
    # print('=' * 20)
    return dp

def reconstruct_path(
    dp: "List[List[List[int]]]",
    i: "int",
    j: "int",
    useList: "bool"=True
) -> "List":
    '''
    reconstruct the solution for shortest path
        from the i th vertex to the j th vertex
        using the dp table

    Params
    ----------
        dp List[List[List[int]]]: 3D dp table that
            has all shortest path
        i int: index of starting vertex
        j int: index of ending vertex

    Returns
    ----------
        List[str] : a list of operations
    '''
    n = len(dp) - 1
    if useList:
        path = []
        reconstruct_helper2(
            dp, i, j, n, path
        )
        return path
    else:
        path = reconstruct_helper1(
            dp, i, j, n
        )
        return path

def reconstruct_helper1(
    dp: "List[List[List[int]]]",
    i: "int",
    j: "int",
    k: "int"
) -> "List[int]":
    '''
    reconstruct solution helper 1

    Params
    ----------
        dp List[List[List[int]]]: 3D dp table that
            has all shortest path
        i int: index of starting vertex
        j int: index of ending vertex
        k: index of the vertex on which making decision
            of going thru or not

    Returns
    ----------
        List[int] : shortest path from i to j
            with the decision of going through k or not
    '''
    if k == 0:
        ## only append vertex when neighbors found
        return [i, j] if dp[0][i][j] < INF else []
    ## if use the current k-1 th vertex gives same distance
    ## as does the use the current k-2 th vertex
    ## doesn't need k-1 th vertex, lose
    if dp[k][i][j] == dp[k - 1][i][j]:
        return reconstruct_helper1(dp, i, j, k-1)
    ## if not, go thru k-1 th
    ## find shortest path between i th and k-1 th
    ## and between k-1 th and j th
    ## ?????why k=k-1?????
    else:
        path1 = reconstruct_helper1(dp, i, k-1, k-1)
        path2 = reconstruct_helper1(dp, k-1, j, k-1)
        ## when merging the two
        ## the end of first half is same as the start of the second half
        path1.extend(path2[1:])
        return path1

def reconstruct_helper2(
    dp: "List[List[List[int]]]",
    i: "int",
    j: "int",
    k: "int",
    ans: "List[int]"
) -> "None":
    '''
    reconstruct solution helper 1

    Params
    ----------
        dp List[List[List[int]]]: 3D dp table that
            has all shortest path
        i int: index of starting vertex
        j int: index of ending vertex
        k: index of the vertex on which making decision
            of going thru or not

    Returns
    ----------
        List[int] : shortest path from i to j
            with the decision of going through k or not
    '''
    if k == 0:
        ## only append vertex when neighbors found
        if dp[0][i][j] < INF:
            ## make sure only append when ans is empty
            ## otherwise the start vertex should be the last end vertex
            if not ans: ans.append(i)
            ans.append(j)
        return
    ## if use the current k-1 th vertex gives same distance
    ## as does the use the current k-2 th vertex
    ## doesn't need k-1 th vertex, lose
    if dp[k][i][j] == dp[k - 1][i][j]:
        reconstruct_helper2(dp, i, j, k-1, ans)
    ## if not, go thru k-1 th
    ## find shortest path between i th and k-1 th
    ## and between k-1 th and j th
    ## ?????why k=k-1?????
    else:
        reconstruct_helper2(dp, i, k-1, k-1, ans)
        reconstruct_helper2(dp, k-1, j, k-1,ans)

## TODO Hirshberg method


def main():
    test_case_1 = [
        [0, 2, -1],
        [3, 0, INF],
        [4, 2, 0]
    ]
    test_case_2 = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    start = time.time()
    for _ in range(10000):
        recur1_ = fw_recur(test_case_1, True)
        recur2_ = fw_recur(test_case_2, True)
    end = time.time()
    dur1 = end - start
    start = time.time()
    for _ in range(10000):
        recur1 = fw_recur(test_case_1)
        recur2 = fw_recur(test_case_2)
    end = time.time()
    dur2 = end - start
    # for rslt in [recur1_, recur2_, recur1, recur2]:
    #     for row in rslt: print(row)
    #     print('\n')
    start = time.time()
    for _ in range(10000):
        dp1 = fw_dp(test_case_1)
        dp2 = fw_dp(test_case_2)
    end = time.time()
    dur3 = end - start
    # ## visualization code
    # print('=' * 20)
    # for plane in dp1:
    #     for row in plane:
    #         print(row)
    #     print('-' * 20)
    # print('=' * 20)
    print(f"duration of recursion with list: {dur1:.4f}")
    print(f"duration of recursion with index: {dur2:.4f}")
    print(f"duration of dp: {dur3:.4f}")
    sol1 = fw_dp(test_case_1)
    # for i in range(len(test_case_1)):
    #     for j in range(len(test_case_1)):
    #         print(f"from {i} to {j}")
    #         print(reconstruct_path(sol1, i, j))
    #         print(reconstruct_path(sol1, i, j, False))
    sol2 = fw_dp(test_case_2)
    # for plane in sol2:
    #     for row in plane:
    #         for ele in row:
    #             print(ele, end='')
    #             if ele != INF: print('\t\t', end='')
    #             print('\t', end='')
    #         print()
    #     print('-'*80)
    # for i in range(len(test_case_2)):
    #     for j in range(len(test_case_2)):
    #         print(f"from {i} to {j}")
    #         print(reconstruct_path(sol2, i, j))
    #         print(reconstruct_path(sol2, i, j, False))
    start = time.time()
    for _ in range(1000000):
        reconstruct_path(sol2, 2, 1)
    end = time.time()
    print(
        "duration of solution build with " \
            + f"list as input: {end - start:.4f}"
    )
    start = time.time()
    for _ in range(1000000):
        reconstruct_path(sol2, 2, 1, False)
    end = time.time()
    print(
        "duration of solution build without " \
            + f"list as input: {end - start:.4f}"
    )
        
    print(reconstruct_path(sol2, 2, 1))

if __name__ == "__main__":
    main()
