# h,m = map(int,input().split())

# if h < 1 and m < 45:
#     h = 23
#     m = m + 15
# elif h < 1 and m >= 45:
#     h = h
#     m = m - 45
# elif h >= 1 and m < 45:
#     h = h - 1
#     m = m + 15
# elif h >= 1 and m >= 45:
#     h = h
#     m = m - 45
# print(h,m)


h,m = map(int,input().split())


if h < 1:
    if m < 45:
        h = 23
        m += 15
    else:
        m -= 45
else:
    if m < 45:
        h -= 1
        m += 15
    else:
        m -= 45
print(h,m)