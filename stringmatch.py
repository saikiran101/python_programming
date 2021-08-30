my_string=input("enter the string").lower()
#print(my_string.upper())
alphabet=input().lower()
count=0
for ch in my_string:
    if ch == alphabet:
        count+=1
print("{}time alphabet is repeted".format(count))
