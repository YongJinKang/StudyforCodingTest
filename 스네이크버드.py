import sys
input = sys.stdin.readline

N, L = map(int, input().split()) 

fruits = list(map(int,input().split()))

fruits.sort()

for fruit in fruits:
    if L >= fruit:
        L += 1

print(L)


    
