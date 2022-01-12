class Solution:
	def removeDups(self, S):
		# code here
		res=''
		for i in S:
		    if i in res:
		        continue
		    res+=i
		return res

#or
def removeDups(self, S): 
    	ns = ''
        al = [0] * 26
        a_val = ord('a')
        for val in S:
            ord_val = ord(val) - a_val
            if al[ord_val] == 1:
                continue
            else:
                ns += val
                al[ord_val] += 1
        return ns