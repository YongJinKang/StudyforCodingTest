n , m = map(int,input().split())
length = list(map(int,input().split()))
length.sort(reverse=True)

for i in range(length[0],0,-1):
    sum1 = []
    for j in length:
        hap = j - i
        if hap <0:
            hap = 0
        sum1.append(hap)
    if sum(sum1) >=  m:
        print(i)
        break
    
        