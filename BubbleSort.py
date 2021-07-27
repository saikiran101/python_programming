def BubbleSort(list):
    for i in range(0,len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

list=[5,3,7,9,10]

print("the unsorted list is: ",list)
print("the sorted list is:",BubbleSort(list))