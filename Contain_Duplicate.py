#class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        dic=[]
#        for i in range(len(nums)):
#            i+=1
#            if i == nums:
#                dic.append(i)
#                return False
#            elif i not in nums:
#                dic.append(i)
#                return True
class Solution:
    def containsDuplicate(self, nums):
        return not (len(nums) == len(set(nums)))

s=Solution()
res=s.containsDuplicate([1,2])
print(res)
