# 1. sorted
# 1) sorted(리스트 또는 문자열)
# 2) 리스트 형태로 리턴
# 3) 문자열 형태로 다시 결합하려면 "".join(sorted(b))

def groupAnagrams():
    input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sorted_arr = [sorted(elem) for elem in input_arr]
    group_len = list(set([tuple(set(elem)) for elem in sorted_arr]))
    group_arr = [[] for _ in range(len(group_len))]
    i = 0

    while len(input_arr) > 0:
        group_arr[i].append(input_arr[0])
        for j in range(1, len(input_arr)):
            if sorted_arr[i] == sorted_arr[j]:
                group_arr[i].append(input_arr[j])
        input_arr = [elem for elem in input_arr if elem not in group_arr[i]]
        i += 1
    print(group_arr)


groupAnagrams()
