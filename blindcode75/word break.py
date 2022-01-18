class Solution:
    def wordBreak(self, s, wordDict):
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:# samply replacing false to true in dp
                    break
        return dp[0]
s=Solution()
res=s.wordBreak("leetcode",["leet","code"])
print(res)
