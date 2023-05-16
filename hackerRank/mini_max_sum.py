def miniMaxSum(arr):
    # sum = math.max(arr)
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    max = sum - arr[0]
    min = sum - arr[4]
    # print(min, max)
    print(min)
    print(max)

arr = [1,2,3,4,5]
miniMaxSum(arr)
print(arr[-2])

print([1]*5)