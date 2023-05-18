def pageCount(n, p):
    # Write your code here
    if not p%2 == 0:
        p = p-1
    print(p)
    page_st = int(p/2)
    page_end = int(((n)-p)/2)
    print((page_st, page_end))
    return min(page_st, page_end)

print(pageCount(6,5))