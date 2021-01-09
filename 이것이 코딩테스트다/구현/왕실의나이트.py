# input_data = input() # 데이터 입력
# row = int(input_data[1]) # 행 데이터 따로 추출
# column = int(ord(input_data[0])) - int(ord('a')) + 1 #열 데이터 따로 추출 ->숫자로
# print(row,column) # 1,1로 확인 가능

# steps = [(-2, -1), (-1, -2), (1, -2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
# # 나이트가 이동할 수 있는 8가지 방향 정의

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0

# for step in steps:
#     #이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row>= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
#         result += 1

# print(result)


#2회차

location = input()

x = int(location[1])
y = (int(ord(location[0])-96))

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

count = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
        continue
    count +=1
    
print(count)
