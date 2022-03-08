class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque as q
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        stack=q([node])
        mapper={node: Node(node.val)}
        while stack:
            cur=stack.popleft()
            for nei in cur.neighbors:
                if nei not in mapper:
                    mapper[nei]=Node(nei.val)
                    stack.append(nei)
                mapper[cur].neighbors.append(mapper[nei])
        return mapper[node]
s=Solution()
res=s.cloneGraph([[2,4],[1,3],[2,4],[1,3]])
print(res)

#need to have graph helper