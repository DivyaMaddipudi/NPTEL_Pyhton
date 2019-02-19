def progression(l):
    if len(l)>2:
        diff = l[1] - l[0]
        for i in range(len(l)-1):
            if not (l[i+1] - l[i] == diff):
                return False
            
        return True
    else:
        return True
print(progression([1,3,5,7,9,11]))
