# Sliding window for requests throtling
# 3 req per 1 sec
# 6 req per 6 sec

arr = [1,1,1,1,2,2,2,3,3,3,7,7,7,7,11,11,11, 11]
w_l = 6
w_max = 6

def get_reqs(c,r,w_l):
    res = 0
    for i in range(r, max(r-w_l,0), -1):
        res += c.get(i, 0)
        
    return res

def get_skip(arr):
    c = dict()
    res = 0
    for r in arr:
        c[r] = c.get(r, 0) + 1
        
        if get_reqs(c, r, w_l) > w_max:
            c[r] = c[r] - 1
            res += 1
        
    return res
    
print(get_skip(arr))