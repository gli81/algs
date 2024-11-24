# -*- coding: utf-8 -*-

'''
implementation of Minimum Spanning Tree algorithms

MST algorithms ...

@author: Gavin Li
@email: liguangzheng998@hotmail.com
@created: 08252024
'''

from typing import List, Tuple
from queue import PriorityQueue

INF: "int" = 10**18

class Vertex():
    def __init__(self, idx: "int", cost: "int") -> "None":
        self.idx = idx
        self.cost = cost

    def __lt__(self, other: "Vertex") -> "bool":
        return self.cost < other.cost

    def __str__(self) -> "str":
        return f"<Vertex: {self.idx}, distance: {self.cost}>"

    def __repr__(self) -> "str":
        return f"<Vertex: {self.idx}, distance: {self.cost}>"


def prim(adjMat: "List[List[int]]") -> "Tuple[List[int], List[int]]":
    '''
    Prim algorithm

    Params
    ----------
        adjMat List[List[int]]: adjacency matrix of the graph
    
    Returns
    ----------
        Tuple[List[int], List[int]] : two lists
            one contains vertex node for each vertex
            the other contains the cost from the tree to the vertex
    '''
    n = len(adjMat)
    visited = [False] * n
    prev = [None] * n
    cost = [INF] * n
    if n <= 1: return prev
    visited[0] = True
    cost[0] = 0
    pq = PriorityQueue()
    for i in range(n):
        if adjMat[0][i] != INF and i != 0:
            cost[i] = adjMat[0][i]
            prev[i] = 0
            pq.put((cost[i], i))
    while not pq.empty() and sum(visited) > 0:
        (_, idx) = pq.get()
        visited[idx] = True
        for i in range(n):
            if i != idx and not visited[i] and adjMat[idx][i] != INF:
                pq.put((adjMat[idx][i], i))
                if adjMat[idx][i] < cost[i]:
                    cost[i] = adjMat[idx][i]
                    prev[i] = idx
    return (prev, cost)

def kruskal(adjMat: "List[List[int]]") -> "List[int]":
    '''
    Kruskal algorithm

    Params
    ----------
        adjMat List[List[int]]: adjacency matrix of the graph
    
    Returns
    ----------
        List[int] : the minimum spanning tree
    '''
    ## create edge list
    n = len(adjMat)
    edges = []
    edges = [
        (adjMat[i][j], (i, j)) 
        for i in range(n) 
        for j in range(i+1, n) 
        if adjMat[i][j] != INF
    ]
    ## sort edge list
    edges.sort(key=lambda x: x[0])
    # print(edges)
    visited = [False] * n
    prev = [-1] * n
    for (_, (st, end)) in edges:
        ## both not visited
        if not visited[st] and not visited[end]:
            visited[st] = True
            visited[end] = True
            prev[end] = st
        ## one visited
        elif not visited[st] and visited[end]:
            prev[st] = end
            visited[st] = True
        ## the other visited
        elif visited[st] and not visited[end]:
            prev[end] = st
            visited[end] = True
        ## both visited => will form circle, don't add
    return prev


def main():
    test_case_1 = [
        [0, 2, 1],
        [2, 0, INF],
        [1, INF, 0]
    ]
    test_case_2 = [
        [0, 3, INF, 7],
        [3, 0, 2, INF],
        [INF, 2, 0, 1],
        [7, INF, 1, 0]
    ]
    test_case_3 = [
        [0, 5, 6, 4, INF, INF],
        [5, 0, 1, 2, INF, INF],
        [6, 1, 0, 2, 5, 3],
        [4, 2, 2, 0, INF, 4],
        [INF, INF, 5, INF, 0, 4],
        [INF, INF, 3, 4, 4, 0]
    ]
    print(prim(test_case_1))
    print(prim(test_case_2))
    print(prim(test_case_3))
    print(kruskal(test_case_1))
    print(kruskal(test_case_2))
    print(kruskal(test_case_3))

if __name__ == '__main__':
    main()
