def flatten(l):
    result = list()
    for i in l:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1,2,[3],[4,[5,6]]]))
