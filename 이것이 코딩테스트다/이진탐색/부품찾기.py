##이진 탐색을 이용한 풀이

def search(array,target,start, end):

    while start <= end:
        mid = (start + end) // 2

        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
total_list = list(map(int,input().split()))
total_list.sort()
m = int(input())
wish_list = list(map(int,input().split()))

for i in wish_list:
    #해당 부품이 존재하는지 확인
    result = search(total_list, i, 0, n-1)
    if result !=None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


## 게수 정렬을 이용한 풀이

# N(가게의 부품 개수)을 입력받기

n = int(input())
array = [0] * 1000001

#가게에 있는 전체 부품 번호를 입력받아서 기록

for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

for i in x:
    #해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


##집합 자료형을 이용한 풀이

n = int(input())
array = list(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
