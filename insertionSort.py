def insertionSort(list):
    #to traverse thourgh 1 to len -1
    for i in range(1,len(list)-1):
        #asign list value to value 
        # and i is right side
         value = list[i]
         #j value also way on left 
         # because of i-1
         j=i -1
         #greater then the value to move one position ahead 
         # of there current position
         while j>=0 and value<list[j]:
             list[j+1]=list[j]
             j-=1
         #result value resign to j+1 to get in order
         list[j+1]=value
    #display
    return list
#driver
list=[3,8,6,2,10]
print("unsorted list:",list)
print("sorted list:",insertionSort(list))