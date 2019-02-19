def valley(l):
    if len(l) > 3:
        for i in range(len(l)):
            if l[i-1]==l[-i]:
                return True
            else:
                return False
        
    return False
print(valley([5,4,3,2,1,2]))