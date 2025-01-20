# -*- coding: utf-8 -*-

from typing import Optional, List

class TreeNode:
    def __init__(
        self,
        val: "int"=0,
        left: "Optional[TreeNode]"=None,
        right: "Optional[TreeNode]"=None
    ):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        ## TODO might want to implement with list in the future
        q = []
        level = 0
        if self: q.append(self)
        while q:
            qsize = len(q)
            for _ in range(qsize):
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            level += 1
        ans = "[" + str(self.val)
        q.append(self.left)
        q.append(self.right)
        cur_level = 1
        while q and cur_level < level:
            qsize = len(q)
            for _ in range(qsize):
                cur = q.pop(0)
                if cur:
                    ans += ", " + str(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    ans += ", None"
                    q.append(None)
                    q.append(None)
            cur_level += 1
        ans += "]"
        return ans

    @classmethod
    def fromList(cls, lst: "List[int]") -> "Optional[TreeNode]":
        if not lst: return None
        n = len(lst)
        if not n: return None
        ans: "List[TreeNode]" = [None] * n
        ans[0] = TreeNode(lst[0]) if lst[0] else None
        for i in range(1, n):
            if lst[i] != None:
                if ans[(i - 1) // 2]:
                    ans[i] = TreeNode(lst[i])
                    if i % 2 == 1:
                        ans[(i - 1) // 2].left = ans[i]
                    else:
                        ans[(i - 1) // 2].right = ans[i]
                else:
                    print("Invalid Input")
                    return None
        return ans[0]