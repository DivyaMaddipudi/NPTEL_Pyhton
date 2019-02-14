def number(n):
        l = []
        for i in range(2,n):
                if i < n:
                        l = l + [i]
        return l                        
#print(number(7))

def prime(m):
        count = 0
        if m > 1:
                for i in range(1,m+1):
                        if m % i == 0:
                                count = count + 1
                if count == 2:
                        return True 
                else:
                        return False
        else:
                return -1
#print(prime(13))

def pp(n):
        s = 0
        x = number(n)
        y = list(filter(prime, x))
        return y
#print(pp(7))



def primepart(num):
        s =0
        n = pp(num)
        m = n.split(',')
        print(m)
        '''for i in range(len(m)):

                return m'''
                
print(primepart(7))
