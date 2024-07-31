
#  https://thought-process-ing.tistory.com/264

# 파트3 공식 사용
    #https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84
import sys

input = sys.stdin.readline
n = int(input())
x_points =[]
y_points =[]

for _ in range(n):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

x_points.append(x_points[0])
y_points.append(y_points[0])

l, r =0, 0
for i in range(n):
    l += x_points[i] * y_points[i+1]
    r += x_points[i+1] * y_points[i]
# print(l, r)
ans = abs(l-r)/2
print(round(ans,1))