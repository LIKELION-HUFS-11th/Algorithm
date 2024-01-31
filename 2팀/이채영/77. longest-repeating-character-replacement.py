class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int(
        :rtype: int
        """
        # 예외 case : [ABBB]
        # global end

        # def find_max_str(blank, char, index):
        #     global end #전역변수: 양쪽에 모두 붙여야 함
        #     if index > len(s)-1:
        #         print("1 and ", end)
        #         return

        #     if s[index] == char:
        #         end = index
        #         print("4 wow")
        #         find_max_str(blank, char, index+1)
        #     else:
        #         if blank > 0: #바꿀 수 있는 기회가 남아있음
        #             end = index
        #             print("3 wow")
        #             find_max_str(blank-1, char, index+1)
        #         elif blank == 0: #최대길이에 도달
        #             print("2 and ", end)
        #             return
   
                    
        # # global end
        # max_str = 0
        # for i in range(len(s)):
        #     blank = 0
        #     if i == 0:
        #         start, end = 0, 0
        #         for j in range(i+1, len(s)):
        #             if s[j] == s[i]:
        #                 end = j
        #                 break
        #             else:
        #                 blank += 1 
        #     elif i > (len(s)-1-max_str): #index out of range 대비
        #         return max_str
        #     else:
        #         start, end = i, i + max_str - 1 #여기서 end=최소end
        #         for j in range(i+1, end+1):
        #             if s[j] != s[i]:
        #                 blank += 1


        #     if end == 0: #i = 1일때 같은 문자가 하나도 없다면
        #         max_str = k + 1

        #     elif blank <= k: #max_len 갱신 가능
        #         find_max_str(k-blank, s[start], end+1)
        #         length = end - start + 1
                
        #         max_str = max(max_str, length)
        #     else:
        #         continue

        #     print("max_str is ", max_str)
                
        # return max_str
    

        #####sol2

        left = right = 0
        counts = collections.Conter()
        for right in range(1, len(s)+1): #오른쪽 포인터를 하나씩 늘리며 범위를 늘려감 
            counts[s[right-1]] += 1 # 오른쪽 포인터와 동일한 문자 수 하나씩 늘림 ex. counts = {"A":1, "B":3}
            max_char_n = counts.most_common(1)[0][1] # counts.most_common(2) = 빈도수 기준 정렬 후 내림차순으로 n개 반환 => [("B", 3), ("A", 1)]
                        `                              # 즉 가장 출현빈도가 높은 문자의 출현빈도수 반환`

            if right - left - max_char_n > k: #right - left - max_char_n = 교체해야 하는 문자 수 
                                                                        # > k일때마다 -> 왼쪽 포인터를 이동해서 범위를 좁혀본다.
                counts[s[left]] -= 1
                left += 1
        return right - left #반복문을 다 돌고 나면 최대구간이 남아있음