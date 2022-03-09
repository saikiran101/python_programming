#class Solution:
#    def pacificAtlantic(self, heights):
#        rows=len(heights)
#        cols=len(heights[0])
#        pacific_reachable=set()
#        atlantic_reachable=set()
#        def dfs(row, col,visited):
#            visited.add((row,col))
#            directions=[(1,0),(0,1),(-1,0),(0,-1)]
#            for r,c in directions:
#                adj_row= row + r
#                adj_col= col + c
#                if adj_row < 0 or adj_col <0 or adj_row >= rows or adj_col >= cols:
#                    continue
#                if (adj_row, adj_col) in visited:
#                    continue
#                if heights[adj_row][adj_col] >=heights[row][col]:
#                    dfs(adj_row, adj_col, visited)
               
#        for i in range(rows):
#            dfs(i,0,pacific_reachable)
#            dfs(i,cols -1, atlantic_reachable)
#        for i in range(cols):
#            dfs(0, i, pacific_reachable)
#            dfs(rows -1,i,atlantic_reachable)
#        return list(pacific_reachable.intersection(atlantic_reachable))

#s=Solution()
#res=s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
#print(res)

from collections import defaultdict, deque

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
PACIFIC = 1
ATLANTIC = 2

class Solution:   
    def pacificAtlantic(self, matrix):
        flow = defaultdict(set)
        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        queue = deque()
        for row in range(rows):
            queue.append((row, 0, PACIFIC))
            queue.append((row, cols - 1, ATLANTIC))
            
        for col in range(cols):
            queue.append((0, col, PACIFIC))
            queue.append((rows - 1, col, ATLANTIC))
            
        while queue:
            row, col, sea = queue.popleft()
            flow[(row, col)].add(sea)
            
            for dr, dc in DIRECTIONS:
                r1 = dr + row
                c1 = dc + col
                if r1 >= 0 and c1 >= 0 and r1 < rows and c1 < cols and matrix[row][col] <= matrix[r1][c1] and sea not in flow[(r1, c1)]:
                    queue.append((r1, c1, sea))
        
        flowboth = []
        for key, seas in flow.items():
            if len(seas) == 2:
                flowboth.append(key)
        
        return flowboth
s=Solution()
res=s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(res)