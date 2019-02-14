def rotatelist(l,n):

        count = 0
        for i in l:
                count = count + 1

                m = n % count

        l = l[m:]+l[:m]

        return l
print(rotatelist([1,2,3,4],2))