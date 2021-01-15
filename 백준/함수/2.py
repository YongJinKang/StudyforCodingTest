def not_selfnumber(n):
    add = 0
    for x in list(str(n)):
        add += int(x) 
    return int(n) + add

not_selfnumber_list= []

for i in range(1,10001):
    k = not_selfnumber(i)
    not_selfnumber_list.append(k)

for b in range(1, 10001):
    if b in not_selfnumber_list:
        pass
    else:
        print(b)
