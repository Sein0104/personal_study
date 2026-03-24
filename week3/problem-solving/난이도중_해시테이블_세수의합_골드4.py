# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# 입력 개수
n = int(input())

# 중복 제거를 위해 set 사용
s = set()

# 숫자 입력 받아서 set에 저장
for _ in range(n):
    s.add(int(input()))

# set → 리스트로 변환 후 정렬
arr = list(s)
arr.sort()

# 두 수의 합을 저장할 집합
sum_set = set()

# arr에 있는 두 수 a, b를 더한 값들을 모두 저장
# (a + b 형태를 미리 계산해둠 → 탐색 속도 향상)
for a in range(n):
    for b in range(n):
        sum_set.add(arr[a] + arr[b])

# 가장 큰 d부터 탐색 (문제에서 "가장 큰 d"를 찾으므로 역순)
for d in range(len(arr)-1, -1, -1):
    # c를 하나 선택해서
    for c in range(len(arr)-1, -1, -1):
        # d = a + b + c  →  d - c = a + b
        # 즉, (d - c)가 sum_set에 있으면 조건 만족
        if (arr[d] - arr[c]) in sum_set:
            print(arr[d])  # 가장 큰 d 출력
            exit()         # 바로 종료