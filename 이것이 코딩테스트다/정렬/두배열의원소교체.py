n,k = map(int,input().split())
print(n,k)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(A,B)

A = sorted(A)
B = sorted(B, reverse=True)

print(A,B)
count = 0
for i in range(len(A)):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
        count += 1
    else:
        pass

    if count == k:
        break

print(f"count:{count}")
print(f"A:{A}")
print(f"B:{B}")
print(f"A 리스트 원소의 합계:{sum(A)}")
    

