def matrixflip(a,b):
    temp=[]
    for i in range(len(a)):
        temp=temp+[a[i][:]]
    if b=='h':
        for i in range(len(temp)):
            temp[i].reverse()
            i=i+1
        return temp
    elif b=='v':
      temp.reverse()
      return(temp) 
print(matrixflip([[1,2],[3,4]],'h'))