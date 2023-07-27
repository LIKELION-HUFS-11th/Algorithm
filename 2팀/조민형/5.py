from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            # 정렬 후 단어로 재조합
            sorted_word = "".join(sorted(word))

            # 해당 정렬된 단어가 result의 key값 중에 있으면 이미 있는 list 형태의 value값에 추가
            if sorted_word in result.keys():
                result[sorted_word].append(word)

            # 정렬된 단어가 result의 key값 중에 없을 경우 key값을 정렬된 단어로 List형태의 새로운 아나그램 value 추가
            else:
                new_group = [word]
                result[sorted_word] = new_group

        return list(result.values())
