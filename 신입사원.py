# import sys

# if __name__ == '__main__':

#     test_case = int(sys.stdin.readline())
#     case1 = int(sys.stdin.readline())
#     C1=[]
#     for i in range(case1):
#         data = tuple(map(int,sys.stdin.readline().split()))
#         C1.append(data)
#     case2 = int(sys.stdin.readline())
#     C2=[]
#     for i in range(case2):
#         data = tuple(map(int,sys.stdin.readline().split()))
#         C2.append(data)

#     C1.sort()
#     C2.sort()

#     count1 = 1
#     count2 = 1
#     for i,j in zip(C1,C1[1:]):
#         if i[1]>j[1]:
#             count1 +=1

#     for i,j in zip(C2,C2[1:]):
#         if i[1]>j[1]:
#             count2 +=1
#     print(count1)
#     print(count2)

import sys
input = sys.stdin.readline
t = int(input())
print(t)
for i in range(t):
    n = int(input())
    print(n)
    s = [0 for i in range(n + 1)]
    print(s)
    for j in range(n):
        a, b = map(int, input().split())
        s[a] = b
        print(s[a])
    min_n = s[1]
    cnt = 0
    for k in range(2, n + 1):
        if s[k] > min_n:
            cnt += 1
        else:
            min_n = s[k]        
    print(n - cnt)

