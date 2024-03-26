import sys

T = int(sys.stdin.readline())

# class Dequeue:
#     def elem(queue):
#         return queue[0]
    
#     def new_queue(queue):
#         queue = queue[1:]
#         return queue
# D = Dequeue()

    # return list(reversed(queue)).pop()

nList = [[]]
for _ in range(T):
    queue =[]
    dic ={} #key는 문서들 예정된 순서, value는 각 문서의 중요도
    
    N, M = map(int, sys.stdin.readline().split())
    #현재 큐에서 M번째 문서의 최종 출력 순서를 알아야함
    nImpt = list(map(int, sys.stdin.readline().split()))#중요도 정보

    
    for idx, elem in enumerate(nImpt):
        dic[idx] = elem
    
    dic = list(dic.items()) #리스트+튜플 형태로 변경
    
    # print(f"dic: {dic}")
    stack =[]
    nAnswer=[] #정답 담을 리스트
    
    # nIdx = 0
    
    if len(dic) == 1:
        # print()
        print(1)
    else:
        while dic:
            # for i in range(1, len(dic)):
            #     if dic[0][1] < dic[i][1]:
            #         dic.append(dic.pop(0))
            #         break
            
            last_elem = dic[-1]
            for elem in dic:
                if dic[0][1] < elem[1]:#중요도 큰놈 생기면 dequeue

                    dic.append(dic.pop(0))
                    # print(f"dic: {dic}")
                    
                    break #dic의 [0]이 바뀌어있을 것임
            
            if last_elem == dic[-1]: #원소가 바뀐 흔적이 없다면
                nAnswer.append(dic.pop(0))

            # elif len(dic) == 1:
            #     nAnswer.append(dic[0])
            #     break

    for i, elem in enumerate(nAnswer):
        if elem[0] == M:
            print(i+1)



    # newDic = sorted(dic.items(), key = lambda x :(-x[1], x[0]))
    # 중요도 내림차순- (중요도 같으면) 프린트 내 순서 오름차순 정렬
    
    # print(list(newDic))

    # for idx, elem in enumerate(list(newDic)): #M값이 어디로 갔는지 찾고,
    #     #(dict에 리스트 씌우면 각 요소들은 튜플로됨)
    #     if elem[0] == M: #최초의 숫자가 일치하면 해당 위치 출력
    #         print(idx+1)
    #         break


    


