def progression(l):
    if len(l)>1:
            
        diff = l[1] - l[0]
        for i in range(len(l)-1):
            if not (l[i+1] - l[i] == diff):
                return False
            
        return True
    else:
        return True
print(progression([3,4,5,7]))
