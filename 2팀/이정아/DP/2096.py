'''
슬라이딩 윈도우 : 공간복잡도 최소화를 위해, 사용 완료한 배열을 새로운 값으로 갱신해 재활용
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
max_dp, min_dp = arr, arr

for _ in range(n-1):
    arr = list(map(int, input().split()))
    max_dp = [max(max_dp[0], max_dp[1]) + arr[0], max(max_dp) + arr[1], max(max_dp[1], max_dp[2]) + arr[2]]
    min_dp = [min(min_dp[0], min_dp[1]) + arr[0], min(min_dp) + arr[1], min(min_dp[1], min_dp[2]) + arr[2]]
    
print(max(max_dp), min(min_dp))