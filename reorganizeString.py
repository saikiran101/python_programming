from collections import Counter
class Solution:
    def reorganizeString(self, s):
        s=Counter(s)
        print(s)


s=Solution()
res=s.reorganizeString("aab")
print(res)