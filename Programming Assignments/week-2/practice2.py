def matched(s):
    depth = 0
    for i in s:
        if i == "(":
            depth = depth + 1
        if i == ")":
            depth = depth - 1
    if depth == 0:
        return True
    else:
        return False
print(matched("((jkl)78(a)&l(8(dd(fji:),):)?)"))