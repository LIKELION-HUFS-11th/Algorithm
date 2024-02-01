class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter_task = Counter(tasks)
        
        result = 0
        while True:
            sub_count = 0

            # task -> 어떤 문자인지
            for task, _ in counter_task.most_common(n+1):
                #sub_count -> idle을 얼마나 넣어야 하는지 계산
                sub_count+=1
                result +=1
                # 꺼낸 문자 카운터에서 삭제
                counter_task.subtract(task)
                # 0이 된 문자 삭제
                counter_task += Counter()
            if not counter_task:
                break
            result += n - sub_count + 1
        
        return result


            
        
