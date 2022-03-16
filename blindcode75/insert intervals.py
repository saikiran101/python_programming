class Solution:
    def insert(self, intervals, newInterval):
        #intervals.append(newInterval)
        #intervals.sort(key=lambda x: x[0])
        
        #result = []
        #for interval in intervals:
        #    if not result or result[-1][1] < interval[0]:
        #        result.append(interval)
        #    else:
        #        result[-1][1] = max(result[-1][1],interval[1])
                
        #return result
        i = 0
        while( i<len(intervals) and intervals[i][0] < newInterval[0]):
            i+= 1
        
        intervals.insert(i,newInterval)
        
        ans = []
        for interval in intervals:
            if len(ans) == 0 or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
    
s=Solution()
res=s.insert([[1,3],[6,9]], [2,5])
print(res)
                