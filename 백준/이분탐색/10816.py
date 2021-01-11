# def search(array,target,start,end):
    
#     while(start<=end):
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid -1
#         else:
#             start = mid + 1

#     return None



n = int(input())

array = list(map(int,input().split()))
array.sort()
m = int(input())

target_list = list(map(int,input().split()))

for target in target_list:
    #해당 부품이 존재하는지 확인
    result = search(array, target, 0, n-1)
    if result !=None:
        print('1', end = ' ')
    else:
        print('0', end = ' ')
