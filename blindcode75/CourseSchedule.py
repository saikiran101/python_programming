from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph=defaultdict(list)
        visit=[0]*(numCourses)
        for course, pre in prerequisites:
            graph[course].append(pre)
        def dfs(course):
            if visit[course] == -1:
                return False
            if visit[course] == 1:
                return True
            visit[course]=-1
            for i in graph[course]:
                if not dfs(i):
                    return False
            visit[course]=1
            return True
        for j in range(numCourses):
            if not dfs(j):
                return False
        return True
s=Solution()
res=s.canFinish(2,[[1,0]])
print(res)