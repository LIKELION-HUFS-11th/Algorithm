inp = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
#정렬되지 않은 배열에서 k번째 큰 요소 추출
#이거 힙 단원임

#아아 최대힙에서 4번째로 추출되는 값을 삭제하면 됨.

#풀이1(교재 예제의 '풀이2')
import heapq
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    
    for _ in range(len(nums) -k):
        heapq.heappop(nums)
        
    return heapq.heappop(nums)


#풀이2
class kth_largest():
    def __init__(self):
        self.n_list = [0]
        
#최대힙의 삽입 함수 통해, 입력받은 배열로 최대 힙 구성
    def heap_insert(self, n): #heap은 기존의 힙, n은 새로 입력할 값임
        heap = self.n_list
        heap.append(n) #일단 n을 힙 맨 뒤에 삽입 -> 완전이진트리 조건 충족 위해.
        i = len(heap) - 1 #삽입된 n의 위치
        
        while i != 1: #1은 루트노드임. 인덱스 값이 0은 비워둠
            pi = i//2 #부모 노드의 인덱스 값. 부모가 값이 더 크다는 최대힙의 조건 충족을 위해.
            if n <= heap[pi]: 
                break #삽입된 값 n이, 부모 노드보다 작다= 문제 없이 추가 완료
            heap[i] = heap[pi] #부모 노드의 값에 자식 노드(처음에는 n) 값을 업데이트=끌어내림
            i = pi #다시 커서가 부모노드 위치로 올라가, 그 위의 부모노드와 다시 비교 시작
        heap[i] = n #최종적으로 올라간 자리에, n값 입력
        
#최대힙의 삭제 함수 = 배열의 최댓값인 루트 값 추출
    #루트 노드를 지우면 기존의 힙트리 조건이 무너질 수 있음. 이걸 고려해야함
    #루트 노드인 사장 자리가 비게되면, 트리 가장 밑 오른쪽 끝에 있는 말단 사원을 사장 자리에 앉힘
    #그러고나서 말단 사원을 순차적으로 비교하면서, 단말 노드까지 강등시켜 본인 자리를 찾아가게 함
    def heappop(self):
        heap = self.n_list
        size = len(heap) -1 #배열에 저장된 힙의 노드 개수. 0번 인덱스는 사용 안함
        if size == 0:
            return None
        
        root = heap[1] #삭제하여 추출할 루트 노드의 값. 현재의 사장 노드의 값
        last = heap[size] #루트 노드로 올라갈 말단 사원 노드의 값
        pi = 1 #삭제할 부모 노드임.
        i = 2 #삭제할 루트 노드의 왼쪽 자식 노드 인덱스
        
        while i <= size: #트리 가장 밑 오른쪽 끝까지 비교
            if heap[i] <= heap[i+1] and i < size: #왼쪽 자식노드보다 오른쪽 자식노드가 더 크면(다운힙 과정)
                i += 1
            if last >= heap[i]: #비교할 자식노드보다, 내려가야할 말단 노드가 더 크다는건, 힙 조건 모두 충족
                break
            
            heap[pi] = heap[i] #조건을 다 충족한 자식 노드(부모 노드보다 값이 더큼)를, 부모노드 자리에 복붙하기
            pi = i #부모 위치가 자식 위치 i로 내려감
            i *= 2  #부모 위치 바뀌었고, 자식노드도 그 다음 비교를 위해, 현재 i의 왼쪽 자식 노드로 내려감
            
        heap[pi] = last #현재 위치한 부모 노드 자리에, 말단 사원이었던 노드의 값을 새롭게 입력해줌
        heap.pop() #아직 맨 마지막에, 그대로 있는 말단 사원 삭제
                
        return root
 
#정답 구성: 삽입 함수로 최대힙 만들고, 삭제 함수를 k번 실시하여 나온 힙의 루트값

#실행
if __name__ == '__main__':
    inp = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    n_list =[0]
    k = 4
    
    kl = kth_largest()
    
    for e in inp:
        kl.heap_insert(e)
        print(kl.n_list[1:])
    
    print('--------------')
    ans = []
    for i in range(k):
        ans.append(kl.heappop())
        print(kl.n_list[1:])
    
    print(ans)
    print(ans[-1])


#아래는 리트코드 양식대로 제출한 코드.
class Solution:
    class kth_largest():
        def __init__(self):
            self.n_list = [0]
            
    #최대힙의 삽입 함수 통해, 입력받은 배열로 최대 힙 구성
        def heap_insert(self, n): #heap은 기존의 힙, n은 새로 입력할 값임
            heap = self.n_list
            heap.append(n) #일단 n을 힙 맨 뒤에 삽입 -> 완전이진트리 조건 충족 위해.
            i = len(heap) - 1 #삽입된 n의 위치
            
            while i != 1: #1은 루트노드임. 인덱스 값이 0은 비워둠
                pi = i//2 #부모 노드의 인덱스 값. 부모가 값이 더 크다는 최대힙의 조건 충족을 위해.
                if n <= heap[pi]: 
                    break #삽입된 값 n이, 부모 노드보다 작다= 문제 없이 추가 완료
                heap[i] = heap[pi] #부모 노드의 값에 자식 노드(처음에는 n) 값을 업데이트=끌어내림
                i = pi #다시 커서가 부모노드 위치로 올라가, 그 위의 부모노드와 다시 비교 시작
            heap[i] = n #최종적으로 올라간 자리에, n값 입력
            
    #최대힙의 삭제 함수 = 배열의 최댓값인 루트 값 추출
        #루트 노드를 지우면 기존의 힙트리 조건이 무너질 수 있음. 이걸 고려해야함
        #루트 노드인 사장 자리가 비게되면, 트리 가장 밑 오른쪽 끝에 있는 말단 사원을 사장 자리에 앉힘
        #그러고나서 말단 사원을 순차적으로 비교하면서, 단말 노드까지 강등시켜 본인 자리를 찾아가게 함
        def heappop(self):
            heap = self.n_list
            size = len(heap) -1 #배열에 저장된 힙의 노드 개수. 0번 인덱스는 사용 안함
            if size == 0:
                return float('-inf')
            
            root = heap[1] #삭제하여 추출할 루트 노드의 값. 현재의 사장 노드의 값
            last = heap[size] #루트 노드로 올라갈 말단 사원 노드의 값
            pi = 1 #삭제할 부모 노드임.
            i = 2 #삭제할 루트 노드의 왼쪽 자식 노드 인덱스
            
            while i <= size: #트리 가장 밑 오른쪽 끝까지 비교
                if i < size and heap[i] <= heap[i+1]: #왼쪽 자식노드보다 오른쪽 자식노드가 더 크면(다운힙 과정)
                    i += 1
                if last >= heap[i]: #비교할 자식노드보다, 내려가야할 말단 노드가 더 크다는건, 힙 조건 모두 충족
                    break
                
                heap[pi] = heap[i] #조건을 다 충족한 자식 노드(부모 노드보다 값이 더큼)를, 부모노드 자리에 복붙하기
                pi = i #부모 위치가 자식 위치 i로 내려감
                i *= 2  #부모 위치 바뀌었고, 자식노드도 그 다음 비교를 위해, 현재 i의 왼쪽 자식 노드로 내려감
                
            heap[pi] = last #현재 위치한 부모 노드 자리에, 말단 사원이었던 노드의 값을 새롭게 입력해줌
            heap.pop() #아직 맨 마지막에, 그대로 있는 말단 사원 삭제
                    
            return root
    
    #정답 구성: 삽입 함수로 최대힙 만들고, 삭제 함수를 k번 실시하여 나온 힙의 루트값
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kl = Solution.kth_largest()

        for e in nums:
            kl.heap_insert(e)


        ans = []
        for i in range(k):
            ans.append(kl.heappop())

        return ans[-1]