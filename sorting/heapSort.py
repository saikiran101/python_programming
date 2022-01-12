from heapq import heappush,heappop
def heapsort(list):
    #inserting list ele in empty arr
    heap=[]
    for ele in list:
        heappush(heap,ele)
    #poping ele from heap
    #inserting the same ele in sort hear 
    # while inserting it will sort elements accordingly
    sort=[]
    while heap:
        sort.append(heappop(heap))
    
    return sort

list=[10,55,45,20,30,100,35,11]
print("heapsort",heapsort(list))
