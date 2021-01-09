n, k = map(int,input().split())
import sys
input = sys.stdin.readline
coins =[]
for i in range(n):
    co = int(input())
    coins.append(co)
coins.sort(reverse=True)
result = 0

for i in range(0,n):
    result += k // int(coins[i]) 
    k = k % int(coins[i]) 

print(result)
