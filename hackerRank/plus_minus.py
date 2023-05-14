def plusMinus(arr):
    # Write your code here
    total_count = len(arr)
    pos = len(filter(lambda i: i>0, arr))
    print(pos, total_count)
    # nag = arr.filter(lambda i: i<0, arr).count()
    # zero = arr.filter(lambda i: i==0, arr).count()
    
    print(pos/total_count)

arr = [1,1,0,-1,-1]
plusMinus(arr)