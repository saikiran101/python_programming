string="aksNIND"
string1=str()
for i in string:
    if i.isupper():
        i=i.lower()
        string1+=i
    else:
        i=i.upper()
        string1+=i
print("the converted string is:{}".format(string1))