class Solution:
    def coinChange(self,coins, amount):
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for curamount in range(1,amount+1):
            for coin in coins:
                if coin <=curamount:
                    dp[curamount]=min(dp[curamount],dp[curamount-coin]+1)
        if dp[amount] >amount:
            return -1
        return dp[amount]

s=Solution()
res=s.coinChange([1,2,5],11)
print(res)