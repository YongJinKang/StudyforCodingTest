import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int,input().split())
    if L+P+V == 0:
        break
    count = 0
    count += L * (V// P)
    if L > (V%P):
        count += V%P
    else:
        count += L
    print('Case %d: %d' %(i, count))
    i += 1

