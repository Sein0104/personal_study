# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
N, M = map(int, input().split())

for i in range (N - M):
  print(i, i + 1)
for j in range (N - M, N - 1):
  print(N - M, j + 1)

"""
N, M = map(int, input().split())
node = [[0, 0] for _ in range (N - 1)]
for i in range (N - M):
  node[i][0] = i
  node[i][1] = i + 1
for j in range (N - M, N - 1):
  node[j][0] = N - M
  node[j][1] = j + 1
print(*node, sep="\n")
"""



"""
N, M = map(int, input().split())

parent = 0
for child in range(1, N):
    print(parent, child)
    if parent < N - M:
        parent += 1
"""



"""
N, M = map(int, input().split())

for i in range(N - 1):
    print(min(i, N - M), i + 1)
"""