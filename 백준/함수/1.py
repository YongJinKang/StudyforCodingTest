import sys

input = sys.stdin.readline

list1=list(map(int,input().split()))

def solve(a):
    return sum(a)

print(solve(list1))