from math import sqrt 
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primesquare(l):
    flag=0
    if len(l)==1:
        n=l[0]
        if(sqrt(n)%1==0):
            return True
    else:
        for i in range(0,len(l)):
            if(sqrt(l[i])%1==0):
                if(i==0):
                    if(isprime(l[i+1])==True):
                        flag=1
                    else:
                        if(isprime(l[i-1])==True):
                            if(isprime[i+1]==True):
                                flag=1
                            else:
                                flag=0
                        else:
                            flag=0

    if(flag==0):
        return False
    else:
        return True

print(primesquare([4,5,9,11]))


'''import math
import operator
def square(l):
    lis = []
    nl = []
    for i in range(len(l)):
        x = l[i] ** 0.5
        lis = lis + [x]
    final = [math.floor(x) for x in lis]
    #return lis
    #return final
    x = list(map(operator.sub,lis,final))
    #return x
    
    for i in x:

        if not i == 0:
            return False

        return True

print(square([16,9,26]))

def prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count = count +1
    if count == 2:
        return True
    else:
        return False
#print(prime(11))

def checkprime(l):
    x = list(filter(prime,l))
    return x
#print(checkprime([2,6,5,7]))

def primesquare(l):
    x = checkprime(l)
    print(l)
    if (l[::2] == x and l[1:][::2]) or (l[1:][::2] and l[::2] == x) :
        return True
#print(primesquare([5,16,101,36,27]))
'''
   



