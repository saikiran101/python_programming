class Solution:
    def longest(self, nums):
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
            
        
s=Solution()
res=s.longest([2,3,4,0,10,11,12])
print(res)