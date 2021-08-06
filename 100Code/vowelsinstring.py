string="saikirAn"
string1=str()
count=0
for i in string.lower():
        if "a"==i or "e"==i or "i"==i or "o"==i or "u"==i:
            count+=1
        else:
            string1+=str(i)
if string1:
    print("remove vowels",string1)
else:
    print("no vowels")

#count the number of vowels
#if count:
#    print("the number of vowels in a string",count)
#else:
#    print("there are no vowels in a string")
