# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

"""
반복문으로 시도
def solution(N, arr)
  
  arr.sort()
  arr1 = [] # 양수
  arr2 = [] # 음수
  for i in range(arr):
    if arr[i] >= 0:
      arr1.append(arr[i])
    else:
      arr2.append(arr[i])

  P = len(arr1)
  M = len(arr2)
  find = arr1[1] + arr2[2]
  for i in range(P):
    for j in range(M):
      A = abs(arr[i] + arr[j])
      if abs(arr[i] + arr[j]) < find:
          find = abs(arr[i] + arr[j])
"""

"""
양수, 음수 나눠서함
잘못된 시도
이유: 문제에 보면 + 나 - 만 있을 수도
def solution(N, arr):
  
  
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
          break

        elif (arr1[i] + arr2[mid]) > 0:
          right = mid - 1

        elif arr1[i] + arr2[mid] < 0:
          left = mid + 1
"""
import random

N = int(input())
arr = list(map(int, input().split(" ")))

def solution(N, arr):
  answer = []
  arr.sort()
  for i in range(N):
    left = 0
    right = N - 1
    
    target = arr[i] * -1

    while left < right:
      mid = (left + right) // 2
      if arr[mid] < target:
        left = mid + 1
      elif arr[mid] > target:
        right = mid - 1
      else:
        answer.append((arr[mid], target))
    
    if (right <= N - 1) and (left != i and right != i):
      if not answer:
        if abs(arr[left] + arr[i]) < abs(arr[right] + arr[i]):
          answer.append((arr[i], arr[left]))
        else:
          answer.append((arr[i], arr[right]))
      else:
       
          x = random.choice(answer)
          if abs(arr[left] + arr[i]) < abs(arr[right] + arr[i]) < abs(x[0] + x[1]):
            answer = [(arr[i], arr[left])]
          elif abs(arr[left] + arr[i]) == abs(x[0] + x[1]):
            answer.append((arr[left], arr[i]))
          elif abs(x[0] + x[1]) == abs(arr[right] + arr[i]):
            answer.append((arr[right], arr[i]))
          elif abs(arr[right] + arr[i])< abs(arr[left] + arr[i]) < abs(x[0] + x[1]):
            answer = [(arr[i], arr[right])]
          
          else:

            if abs(arr[left] + arr[i]) < abs(arr[right] + arr[i]):
              answer.append((arr[left], arr[i]))
            else:
              answer.append((arr[right], arr[i]))
  x = random.choice(answer)
  print(x[0], x[1])

solution(N, arr)
