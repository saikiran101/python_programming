class Solution:
    def findDisappearedNumbers(self, nums):
        result=set(nums)
        e=[]
        for i in range(1,len(nums)+1):
            if i not in result:
                e.append(i)
        return e
s=Solution()
res=s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(res)