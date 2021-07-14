string='sai'
for i in range(1,len(string)+1):
    for lenght in range(len(string)- i +1):
        print(string[lenght:lenght + i])

        