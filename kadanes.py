def maxSubArraySum(a,size):
        ##Your code here
        maxh=a[0]
        maxg=a[0]
        for i in range(1,size):
            maxh=max(a[i],maxh+a[i])
            maxg=max(maxh,maxg)
        return maxg



#def maxSubArraySum(a,size):
     
#    max_so_far = a[0]
#    max_ending_here = 0
     
#    for i in range(0, size):
#        max_ending_here = max_ending_here + a[i]
#        if max_ending_here < 0:
#            max_ending_here = 0
         
#        # Do not compare for all elements. Compare only  
#        # when  max_ending_here > 0
#        elif (max_so_far < max_ending_here):
#            max_so_far = max_ending_here
             
#    return max_so_far
  
# Driver function to check the above function
a = [1,2,3,-2,5]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))