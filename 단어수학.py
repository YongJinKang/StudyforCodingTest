import sys
input = sys.stdin.readline

n = int(input())

po=[]
ne=[]
for i in range(n):

    data = (int(input()))
    if data >= 0:
        po.append(data)
    else:
        ne.append(data)

po.sort(reverse=True)
ne.sort()
result = 0

for i,j in zip(po,po[1:]):
    for k,l in zip(ne,ne[1:]):
        if (int(i)*int(j))>=(int(k)*int(l)):
            
            while True:
                if i == 1:
                    result *= po[i]
                else:
                    result += po[i]
                    result += ne[i]
        else:
            for i in range(n):
                if i ==1:
                    result *= ne[i]
                else:
                    result += ne[i]
                    result += po[i]

print(result)
            



