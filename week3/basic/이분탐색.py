# def solution(N, arr)
  
#   arr.sort()
#   arr1 = [] # 양수
#   arr2 = [] # 음수
#   for i in range(arr):
#     if arr[i] >= 0:
#       arr1.append(arr[i])
#     else:
#       arr2.append(arr[i])

#   P = len(arr1)
#   M = len(arr2)
#   find = arr1[1] + arr2[2]
#   for i in range(P):
#     for j in range(M):
#       A = abs(arr[i] + arr[j])
#       if abs(arr[i] + arr[j]) < find:
#           find = abs(arr[i] + arr[j])

def solution(N, arr)
  
  
  arr1 = [] # 양수
  arr2 = [] # 음수
  for i in range(arr):
    if arr[i] >= 0:
      arr1.append(arr[i])
    else:
      arr2.append(arr[i])

  arr1.sort()
  arr2.sort()
  P = len(arr1)
  M = len(arr2)
  
  for i in range(len(arr2)):
      left = 0
      right = P - 1

      while left <= right:
        mid = (left + right) // 2

        if arr1[i] + arr2[mid] == 0:
          print (arr1[i], arr[mid])

        elif (arr1[i] + arr2[mid]) > 0:
          right = mid - 1

        elif arr1[i] + arr2[mid] < 0:
          left = mid + 1