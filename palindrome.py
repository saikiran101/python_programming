def palindrome(n):
    return n==n[::-1]



#driver
n="111"
solution=palindrome(n)

if solution:
    print("Yes")
else:
    print("No")