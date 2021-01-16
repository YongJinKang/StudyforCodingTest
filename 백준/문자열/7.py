n,m = map(int,input().split())

n1 = (n // 100) 
n2 = (n % 100) // 10
n3 = (n % 10)

n = (n3*100)+(n2*10)+(n1)

m1 = (m // 100) 
m2 = (m % 100) // 10
m3 = (m % 10)

m = (m3*100)+(m2*10)+(m1)

if n>m:
    print(n)
else:
    print(m)