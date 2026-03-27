# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

n = int(input())

def sein(n):
  dp = [0  for _ in range (n + 1)]
  if n <= 1:
    return 1
  dp[0] = 1
  dp[1] = 1
  for i in range(2, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
  return dp[n]
  
print(sein(n))
