class Solution:
    def besttimetobuy(self,prices):
        max_profit=0
        higher=0
        prices=prices[::-1]
        for price in prices:
            if price>higher:
                higher=price
            if higher - price>max_profit:
                max_profit=higher- price
        return max_profit
s=Solution()
res=s.besttimetobuy([7,1,5,3,6,4])
print(res)