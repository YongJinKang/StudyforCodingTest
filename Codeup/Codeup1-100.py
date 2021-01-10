# 19
# y,m,d = input().split(".")
# print("%04d"%int(y),"%02d"%int(m),"%02d"%int(d), sep=".")

# 20
# front, back = input().split("-")
# print(front+back)

# 21
# char = input()
# print(str(char))

# 22
# sentence = input()
# print(str(sentence))

# 23
# front, back = input().split('.')
# print(int(front))
# print(int(back))

#24
# word = input()
# list=[]
# for i in range(len(word)):
#     letter = "'"+word[i]+"'"
#     list.append(letter)

# for i in range(len(list)):
#     print(list[i])
# word = "letter"
# for i in range(len(word)):
#     print(word[i])

#25
# number = input()
# list=[]
# for i in range(len(number)):
#     n = number[i]
#     list.append(n)


# for i in range(len(list)):
#     answer = int(list[i])*int(10)**int(len(list)-(i+1))
#     print("[%d]"%answer)

#26.

# hh,mm,ss = input().split(":")
# print("%0d"%int(mm))

#27.

# yyyy,mm,dd = input().split(".")

# print("%02d"%int(dd),"%02d"%int(mm),"%04d"%int(yyyy),sep="-")

#28.
# number = input()

# print("%.11f"%float(number))

#34.

# number= int(input(), 8)
# print(number)

#35.
# number= int(input(), 16)
# b = oct(number)

# print(b[2:])

#36.

# a, b = input().split(" ")

# print(int(a)+int(b))

# a = -int(input())
# print(a)
# a, b = input().split(" ")
# print(int(a) // int(b))

#43.
# a, b = input().split(" ")
# print(int(a) % int(b))

#44.
# a = input()
# print(int(a)+1)

#45.

# a, b = input().split(" ")
# a = int(a)
# b = int(b)
# def pp(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a//b)
#     print(a%b)
#     print("%.2f"%float(a/b))

# pp(a,b)


# a, b, c = input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)
# def cal(a, b, c):
#     print(a+b+c)
#     print("%.1f"%float((a+b+c)/3))

# cal(a,b,c)

# num = input()
# print(int(num)*2)


# a,b = input().split(" ")
# print(int(a)*2**int(b))

# a,b = input().split(" ")
# if int(a)>int(b):
#     print(1)
# else:
#     print(0)

# a,b = input().split(" ")
# if int(a) == int(b) :
#     print(1)
# else:
#     print(0)

# a,b = input().split(" ")
# if int(a) <= int(b):
#     print(1)
# else:
#     print(0)

# a,b = input().split(" ")
# if int(a) != int(b):
#     print(1)
# else:
#     print(0)

# a = input()
# if int(a) == 0:
#     print(1)
# elif int(a) == 1:
#     print(0)

# a,b = input().split(" ")

# if int(a) == 1 and int(b) == 1:
#     print(1)
# else:
#     print(0)

# a,b = input().split(" ")
# if int(a) == 1 or int(b) == 1:
#     print(1)
# else:
#     print(0) 

# a,b = input().split(" ")

# if int(a) != int(b):
#     print(1)
# else:
#     print(0)

# a,b = input().split(" ")

# if int(a) == int(b):
#     print(1)

# else:
#     print(0)

# a,b = input().split(" ")

# if int(a) == 0 and int(b) == 0:
#     print(1)
# else:
#     print(0)

# a = input()
# print("%d"%~int(a))

# a,b = input().split(" ")
# a = int(a)
# b = int(b)
# print("%d"%(a & b))

# a, b = input().split(" ")
# a = int(a)
# b = int(b)

# print("%d"%(a | b))

# a, b = input().split(" ")
# a = int(a)
# b = int(b)

# print(a if a>b else b)

# a, b, c = input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else:
#     print(c)

# a, b, c = input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)

# list = []
# list.append(a)
# list.append(b)
# list.append(c)

# for i in list:
#     if i%2==0:
#         print(i)

# a, b, c = input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)

# list = []
# list.append(a)
# list.append(b)
# list.append(c)

# for i in list:
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")


# a = input()
# a = int(a)

# if a>0:
#     print("plus")
# else:
#     print('minus')
# if a%2==0:
#     print("even")
# else:
#     print('odd')

# a = int(input())

# if a >= 90:
#     print("A")
# elif a >= 70:
#     print("B")
# elif a >= 40:
#     print("C")
# elif a >= 0:
#     print("D")

# a = str(input())

# if a == "A":
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else:
#     print("what?")

# a = int(input())

# if a==12 or a<=2:
#     print("winter")
# elif a<=5:
#     print("spring")
# elif a<=8:
#     print("summer")
# elif a<=11:
#     print("fall")


# list = input().split(" ")
# for i in range(len(list)):
#     list[i]=int(list[i])
#     if list[i] == 0:
#         break
#     print(list[i])

# count = int(input())
# list_index = input().split(" ")
# # print(count)
# # print(list_index)

# for i in range(count):
#     print(int(list_index[i]))

# list = input().split(" ")
# for a in list:
#     if a == '0':
#         break
#     print(a)

# list = input().split(" ")

# for a in list:
#     if a != '0':
#         print(a)
#     else:
#         break

# a = int(input())

# for i in range(a):
#     print(a-i)

# a = ord(input())


# for i in range(a-96):
#     print(chr(i+97))

# a = int(input())

# for i in range(a+1):
#     print(i)

# a = int(input())

# sum = 0

# for i in range(1,a+1):
    
#     if i%2==0:
#         sum += i

# print(sum)

# list_index = input().split(" ")
# for l in list_index:
#     print(l)
#     if l == 'q':
#         break


# num = int(input())

# sum = 0

# for i in range(1,num+1):
#     if num <= sum:
#         print(i-1)
#         break
#     else:
#         sum += i
        
        
# n,m = input().split(" ")
# n = int(n)
# m = int(m)

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)

# num = input()

# num = int(num, 16)

# for i in range(1,16):
#     print("{}*{}={}".format(hex(num)[2:].upper(),hex(i)[2:].upper(),hex(num*i)[2:].upper()))
#     # print(f"{hex(num)[2:].upper()}*{hex(i)[2:].upper()}={hex(num*i)[2:].upper()}")


# num = int(input())
# for i in range(1,num+1):
#     if i % 3 == 0:
#         print('X',end=' ')
#     else:
#         print(i,end=' ')
  
# R,G,B = input().split(" ")
# R = int(R)
# G = int(G)
# B = int(B)
# count = 0
# for r in range(R):
#     for g in range(G):
#         for b in range(B):
#             print("{} {} {}".format(r,g,b)) 
#             count += 1
# print(count)

# h, b, c, s = input().split(" ")
# h = int(h)
# b = int(b)
# c = int(c)
# s = int(s)

# answer=(((h*b*c*s)/8)/1024)/1024

# print("%.1f"%answer,"MB")

# w, h, b = input().split(" ")
# w = int(w)
# h = int(h)
# b = int(b)

# answer=(((w*h*b)/8)/1024)/1024

# print("%.2f"%answer,"MB")

# num = int(input())

# sum = 0

# for i in range(1, num+1):
#     # print(i)
#     if sum < num:
#         sum = sum + i
#     else:
#         break

# print(sum)

# num = int(input())

# for i in range(1,num+1):
#     if i%3!=0:
#         print(i, end=' ')

# a, d, n = input().split(" ")

# a = int(a)
# d = int(d)
# n = int(n)

# for i in range(n-1):
#     a += d
# print(a)
# from math import gcd

# def lcm(a,b):
#     return a*b // gcd(a, b)


# n1, n2, n3 = input().split(" ")

# n1 = int(n1)
# n2= int(n2)
# n3 = int(n3)

# print(lcm(lcm(n1,n2),n3))

# time = int(input())

# list_index = map(int,input().split())
# list_index=list(list_index)
# list1 = []

# for i in range(24):
#     list1.append(0)  

# for i in range(time):
#     list1[list_index[i]] += 1

# for i in range(1, 24):
#     print(list1[i], end = ' ')

# n1 = int(input())
# n2 = map(int, input().split())
# n2 = list(n2)
# n3 = []

# for i in range(n1):
#     n3.append(0)

# for i in range(n1):
#     n3[n1-1-i]=n2[i]

# for i in range(n1):
#     print(n3[i], end=' ')

# n1 = int(input())
# n2 = map(int, input().split())
# n2 = list(n2)

# print(min(n2))

# n = int(input())

# m = [ [0 for col in range(20)] for row in range(20)]

# for i in range(n):
#     x, y = input().split()
#     m[int(x)][int(y)] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(m[i][j], end = ' ')
#     print('')

# n = int(input())

# m = [ [0 or 1 for col in range(20)] for row in range(20)]

# print(m)
# for i in range(n):
#     x, y = input().split()
#     m[int(x)][int(y)] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(m[i][j], end = ' ')
#     print('')

# map = []

# for i in range(19) :
#     map.append(input().split())

# n = int(input())

# for i in range(n):
#     x, y = input().split()
#     x, y = int(x) -1, int(y) - 1
#     for j in range(19):
#         if(map[j][y] == '0'):
#             map[j][y] = '1'
#         else:
#             map[j][y] == '0'
#         if(map[x][j] == '0'):
#             map[x][j] = '1'
#         else:
#             map[x][j] = '0'

# for i in range(19):
#     for j in range(19):
#         print(map[i][j], end = ' ')
#     print()


# h , w = input().split()

# h , w = int(h), int(w)

# m = []

# for i in range(h):
#     m.append([])
#     for j in range(w):
#         m[i].append(0)
# n = int(input())
# for i in range(n):
#     l, d, x, y = input().split()
#     for j in range(int(l)):
#         if(int(d) ==0):
#             m[int(x) -1][int(y) -1 + j] = 1
#         else:
#             m[int(x) - 1 + j][int(y) - 1] = 1

# for i in range(h):
#     for j in range(w):
#         print(m[i][j], end =' ')
#     print()

# m = []

# for i in range(20):
#     m.append([])
#     for j in range(20):
#         m[i].append(0)

# for i in range(19) :
#     a = input().split()

#     for j in range(19):
#         m[i+1][j+1] = int(a[j])

# n = int(input())

# for i in range(n):
#     x, y = input().split()
#     for j in range(1, 20):

#         if m[j][int(y)] == 0 :
#             m[j][int(y)] = 1
#         else:
#             m[j][int(y)] =  0

#         if m[int(x)][j] == 0:
#             m[int(x)][j] = 1
#         else:
#             m[int(x)][j]  = 0

# for i in range(1, 20):
#     for j in range(1, 20) :
#         print(m[i][j], end = ' ')
#     print()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        m[i].append(0)
for i in range(10) :
    a = input().split()
    for j in range(10):
        m[i+1][j+1] = int(a[j])
x = 2
y = 2

while True:
    if m[x][y] == 0:
        m[x][y]=9
    elif m[x][y]==2:
        m[x][y]=9
        break

    if (m[x][y+1] == 1 and m[x+1][y] == 1) or (x ==9 and y ==9) :
        break

    if m[x][y+1]!=1:
        y+=1
    elif m[x+1][y] !=1:
        x+=1
for i in range(1, 11):
    for j in range(1,11):
        print(m[i][j], end = ' ')
    print()

    


