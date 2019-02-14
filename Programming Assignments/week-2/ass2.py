def nestingdepth(s):
    depth = 0
    maxval = 0
    for i in s:
        if i == "(":
            depth = depth + 1
            if depth > maxval:
                maxval = depth
        elif i == ")":
            if depth != 0:
                depth = depth - 1
            else:
                return maxval
    
    if depth != 0:
        return -1
    else:
        return maxval
print(nestingdepth("((jkl)78(a)&l(8(dd(fji:),):)?"))
