class Solution:
    def CountBits(self,n):
        dp=[0]
        for i in range(1,n+1):
            if i%2==1:
               dp.append(dp[i-1]+1)
            else:
               dp.append(dp[i//2])
        return dp

s=Solution()
res=s.CountBits(5)
print(res)