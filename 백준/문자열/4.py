n = int(input())
for i in range(n):
    r, s = input().split()
    repeat = ''
    for i in s:
        repeat+= i * int(r)
    print(repeat)
