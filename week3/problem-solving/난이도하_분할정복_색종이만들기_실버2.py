# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

white_count = 0
blue_count = 0
N = int(input())
arr = []

for i in range(N):
  arr.append(list(map(int, input().split(" "))))

def paper(N, x, y):
  global white_count
  global blue_count
  
  for i in range(x, x+N):
    for j in range(y, y+N):
      if arr[x][y] != arr[i][j]:
        size = N // 2
        paper(size, x, y)
        paper(size, x, y + size)
        paper(size, x + size, y)
        paper(size, x + size, y + size)
        return
  if arr[x][y] == 1:
    blue_count += 1
  else:
    white_count += 1
  

paper(N, 0, 0)
print(white_count, blue_count, sep='\n')



