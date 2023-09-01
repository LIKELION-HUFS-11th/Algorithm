n = int(input())
sentence_list = []
for _ in range(n):
    sentence_list.append(list(input()))

alphabet_dic = {}

for sentence in sentence_list:
    l = len(sentence) - 1
    for alphabet in sentence:
        if alphabet in alphabet_dic:
            alphabet_dic[alphabet] += 10**l
        else:
            alphabet_dic[alphabet] = 10**l
        l -= 1

alphabet_dic =sorted(alphabet_dic.items(), key=lambda x: x[1], reverse=True)

total = 0
num = 9
for alphabet in alphabet_dic:
    total += alphabet[1] * num
    num -= 1

print(total)