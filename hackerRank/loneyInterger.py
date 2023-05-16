def lonelyinteger(a):
    # Write your code here
    res = {}
    for i in range(len(a)):
        if a[i] in res:
            print(res[a[i]])
            del res[a[i]]
        else:
            res[a[i]] = 1
    return res.keys()[0]
  


lonelyinteger([1,2,3,4,3,2,1])