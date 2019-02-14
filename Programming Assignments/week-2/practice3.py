def prime(n):
    count = 0
    if n > 1:
        for i in range(1,n+1):
            if n % i == 0:
                count = count + 1        
        if count == 2:
            return True
        else:
            return False
#print(prime(11))

def sumprimes(l):
    x = list(filter(prime,l))
    y = sum(x)
    return y
print(sumprimes([17,51,29,39]))
