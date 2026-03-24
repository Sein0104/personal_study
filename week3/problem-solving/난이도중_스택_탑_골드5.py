# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

"""
현재 탑보다 낮은 탑은 수신이 불가, 그냥 통과함
 -> 기존에 있던 왼쪽 탑 중에서 현재 탑 보다 높은게 있어야함

수신 탑 후보들을 담은 리스트 = stack
스택에 후보 탑 넣는 형식: (순서, 높이)

스택 i 번째 탑의 출력 방식
순서 출력: stack[i][0]
높이 출력: stack[i][1] 

후보 중에서 현재 검사하는 탑 보다 낮다면? pop
스택이 텅 비게 된다면? 자신보다 큰 탑이 없는거임! 수신불가 -> 결과에 0 추가
현재 검사하는 탑보다 높으면 -> 결과에 탑 순서 추가

"""
N = int(input())       # 탑의 개수
tower = list(map(int, input().split()))      # 탑들을 담을 리스트

def tower_high(N, tower):

  stack = []     # 스택 설정
  answer = []     # 결과값 담을 리스트

  for i in range(N):    # N 개의 탑 검사
    h = tower[i]      # h = 검사할 탑(높이)
    while stack and stack[-1][1] < h:    # 스택이 비어있지 않음 and 후보 높이가 h 보다 작으면
      stack.pop()      # 수신할 탑 후보에서 제외
    if not stack:     # 스택이 비어있으면
      answer.append(0)      # 결과에 0 추가
      stack.append((i, h))     # 스택에는 현재 탑 추가
    else:      # stack[-1][1] > h
      answer.append(stack[-1][0] + 1)     # 결과에 추가: 수신 탑의 번호
      stack.append((i, h))      # 스택에 현재 탑을 후보로 추가
  print(*answer)
      
tower_high(N, tower)        



