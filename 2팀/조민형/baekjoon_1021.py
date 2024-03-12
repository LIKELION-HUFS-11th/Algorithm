import sys

def queue_active(queue_list, search_num):
    result = 0
    # 왼쪽이 더 최적화일 때
    if queue_list.index(search_num) < len(queue_list) - queue_list.index(search_num):
        for _ in range(queue_list.index(search_num)):
            popped = queue_list.pop(0)
            queue_list.append(popped)
            result +=1
        del(queue_list[0])
        return result
    else:
        for _ in range(len(queue_list) - queue_list.index(search_num)):
            popped = queue_list.pop(len(queue_list)-1)
            queue_list.insert(0,popped)
            result +=1
        del(queue_list[0])
        return result

N, M = map(int,sys.stdin.readline().split())

sequential_list = []
for i in range(1,N+1):
    sequential_list.append(i)

circular_list = list(map(int,sys.stdin.readline().split()))
count = 0
for j in range(M):
    count += queue_active(sequential_list,circular_list[j])
print(count)
