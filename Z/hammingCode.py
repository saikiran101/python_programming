def max_block_sum(arr):
    def rotateby1(arr):
        n = len(arr)
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i + 1]
        arr[n-1] = temp
    max_sum = 0
    def find_block_sum(arr):
        sum = 0
        for (idx, val) in enumerate(arr):
            sum += val * (idx + 1)
        print(sum)

        return sum
    for i in range(len(arr)):
        max_sum = max(max_sum, find_block_sum(arr))
        print(arr)
        rotateby1(arr)

    return max_sum

res = max_block_sum([30,10,35,27,35])
print(res)