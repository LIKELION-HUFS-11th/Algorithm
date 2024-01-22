# 시작 지점에서 도착 지점으로 가는 데 가장 빠른 경로
# 선택지가 걷기와 순간이동이 있는데
# 걷기 -> 현재위치+1 or 현재위치-1 위치로 이동
# 순간이동 -> 0초 후에 현재위치의 2배 위치로 이동
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


start, sister = tuple(map(int,input().split()))

distance = [[INF] for _ in range()] #최단 거리 리스트

def dijkstra(start):
