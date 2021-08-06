def palindrome(n):
    return n==n[::-1]

n="sas"
string=palindrome(n)
if string:
    print("the given string is a palindrome",string)
else:
    print("it is not a palindrome")
