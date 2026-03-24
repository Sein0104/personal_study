# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

# 보드 정의 ( 0: 빈칸, 1: 뱀, 4: 사과 )
n = int(input())
board = [[0] * n for _ in range(n)]  

# 사과 정의
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 4

# 방향전환 정의
l = int(input())
turns = deque()
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))

# 뱀 몸통: 꼬리(popleft) -> 머리(append) 순서로 큐 저장
snake = deque([(0, 0)])
board[0][0] = 1

# 초기 이동 및 시간정보 선언
dr, dc = 0, 1
time = 0

# 종료할 때까지 움직임
while True:
    time += 1

    # 1. 현재 머리좌표 정의
    hr, hc = snake[-1]

    # 2. 머리가 이동하려는 board 좌표 계산
    nr, nc = hr + dr, hc + dc

    # 3. [종료] 벽 또는 자기 몸 충돌
    if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == 1:
        print(time)
        break

    # 4. board에 머리 추가
    snake.append((nr, nc))

    # 4-1. 사과가 있으면 꼬리 유지
    if board[nr][nc] == 4:
        board[nr][nc] = 1

    # 4-2 사과가 없으면 꼬리 한 마디 제거
    else:
        board[nr][nc] = 1
        tr, tc = snake.popleft()
        board[tr][tc] = 0

    # 5. 이동 완료 후, 방향 전환 인자 확인
    if len(turns) > 0 and turns[0][0] == time:
            _, direction = turns.popleft()

            if direction == 'D':
                # case 1. 오른쪽 90도 회전
                dr, dc = dc, -dr
            else:
                # case 2. 왼쪽 90도 회전
                dr, dc = -dc, dr