l, c = map(int, input().split())
letters = list(input().split())

'''
[재귀, 백트래킹]
1. 모음 1개 이상, 자음 2개 이상, 알파벳 순대로 조합한 비밀번호 l자리 차례대로 출력
'''

letters.sort() # 후보 알파벳들 사전순으로 정렬

ans = []
vowels = ["a", "e", "i", "o", "u"]

def lock(idx, depth):
    if depth == l: # l자리만큼 다 모였으면
        vowel, consonant = 0, 0
        for letter in ans:
            if letter in vowels:
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2: # 모음 1자리 이상, 자음 2자리 이상이면 출력
            print("".join(ans))
        return
    
    for i in range(idx, c):
        ans.append(letters[i])
        lock(i+1, depth+1)
        ans.pop()
    
lock(0, 0)