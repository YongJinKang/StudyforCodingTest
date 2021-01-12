# h,m = map(int,input().split())

# if h < 1 and m < 45:
#     h = 23
#     m = m + 15
# elif h < 1 and m >= 45:
#     h = h
#     m = m - 45
# elif h > 1 and m < 45:
#     h = h - 1
#     m = m + 15
# elif h > 1 and m >= 45:
#     h = h
#     m = m - 45
# print(h,m)

h,m = map(int,input().split())

if h < 1 and m < 45:
    h = 23
    m = m + 15
elif h < 1 and m >= 45:
    h = h
    m = m - 45
elif h >= 1 and m < 45:
    h = h - 1
    m = m + 15
elif h >= 1 and m >= 45:
    h = h
    m = m - 45
print(h,m)

if m < 45:
    m = m + 15
    if h < 1:
        h = 23
    else:
        h = h - 1
else:
    m = m - 45