class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for first in range(len(nums)-2):
            if first>0 and nums[first]==nums[first-1]:
                continue
            second,third=first+1,len(nums)-1
            while second<third:
                s= nums[first]+nums[second]+nums[third]
                if s<0:
                    second+=1
                elif s>0:
                    third-=1
                else:
                    res.append([nums[first],nums[second],nums[third]])
                    while second<third and nums[second]==nums[second+1]:
                        second +=1
                    while second<third and nums[third]==nums[third-1]:
                        third-=1
                    second+=1
                    third-=1
        return res

s=Solution()
res=s.threeSum([-1,0,1,2,-1,-4])
print(res)
