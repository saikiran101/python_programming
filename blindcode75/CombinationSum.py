class Solution:
    def combinationSum4(self, N, T):
        dp = [0] * (T + 1)
        dp[0] = 1
        for i in range(1, T+1):
            for num in N:
                if num <= i:dp[i] += dp[i-num]
        return dp[T]
        
s=Solution()    
res=s.combinationSum4([1,2,3],4)
print(res)