def descending(l):
    li = []
    for i in l:
        li = li + [i]
    x = l
    x.sort(reverse = True)
    if li == x:
        return True
    else:
        return False

print(descending([]))