'''
[단어 수학]
https://www.acmicpc.net/problem/1339
'''
n = int(input())
letter_dict = dict()
for _ in range(n):
    word = list(input())
    length = len(word)
    for i in range(length):
        if word[i] in letter_dict:
            letter_dict[word[i]] += 10 ** (length - i - 1)
        else:
            letter_dict[word[i]] = 10 ** (length - i - 1)

sorted_dict = sorted(letter_dict.items(), key=lambda x : -x[1])

max_sum, num = 0, 9
for _, sum in sorted_dict:
    max_sum += sum * num
    num -= 1
print(max_sum)
