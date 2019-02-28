def rainaverage(l):
    sum = dict()
    count = dict()
    for (k, v) in l:
        sum[k] = sum.get(k, 0) + v
        count[k] = count.get(k, 0) + 1
    for k in sum:
        sum[k] /= count[k]
    res= list(sum.items())
    res.sort()
    return res
print(rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)]))