t = int(input())
data = []

# 회문인지 검사하는 함수
def is_palindrome(word):
    n = len(word)
    for index in range(n // 2):
        if word[index] != word[n - 1 - index]:
            return False
    return True

# 유사회문인지 검사하는 함수
def is_pseudo(word):
    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            modified_word1 = word[:i] + word[i + 1:]
            modified_word2 = word[:n - 1 - i] + word[n - i:]
            return is_palindrome(modified_word1) or is_palindrome(modified_word2)
    return True

# 입력 받기
for _ in range(t):
    data.append(input())

# 검사 및 결과 출력
for word in data:
    if is_palindrome(word):
        print(0)
    elif is_pseudo(word):
        print(1)
    else:
        print(2)


# # #len = 4
# # # len // 2 = 2
# # # 1 2 3 4
# # # 1 2 3 4 5
# # # 1 2 3 4 5 6

# # ## 회문이려면

# # # len = 6이면
# # # [0] == [5]
# # # [1] == [4]
# # # [2] == [3]

# # # len == 5이면
# # # [0] == [4]
# # # [1] == [3]
# # # [2] == [2]


# # n = len(word)


# # 아래가 회문 체크하는 코드
# # for index in range(n):
# #     while index < n // 2: 
# #         if word[index] != word[n-1 - index]:
# #             break

# # # 유사 회문의 특징
# # # 반으로 띡 잘랐을 때 
# # # 3(n//2=3)을 기준으로 자르면
# # # s u m 과 m u u s로 자르면 됨
# # # 0 1 2    3 4 5 6 

# # # x a b b a 는 반으로 띡 잘랐을 때
# # # 2(n//2=2)를 기준으로 자르면 됨
# # # x a b 와 b a 

# # # c o m w w t m o c
# # # 4(n//2=4)를 기준으로 자르면 됨
# # # c o m w 와 w t m o c 
# # # 0 1 2 3 4 5 6
# # # s u m m u u s
# # 슬라이싱해서 뭉텅이 끼리 비교
# # summmuus를 예로 들면은
# # word[0:index//2] 와 word[index//2:]로 뭉텅이를 나누고
# # 두 번째 뭉텅이는 거꾸로 돌려서 비교를 하는 거야

# # first_word = word[0:index//2]
# # second_word = word[index//2:]

# # # 비교하기 쉽게 거꾸로 돌림
# # for i in range(n-1, 0, -1):
# #     while n-1-i >= 0:
# #         second_word[i] = second_word[n-1 -i] # 6은 0으로 5는 1로
# # first_word와 second_word 비교

# ## 입력
# t = int(input())
# data = []
# for _ in range(t):
#     data.append(input())
# check = []

# # 회문인지 검사하는 함수
# def palindrome(word):
#     n = len(word)
#     for index in range(n):
#         while index < n // 2: 
#             if word[index] != word[n-1 - index]:
#                 break
#     else:
#         return palindrome
    
# def is_palindrome(substring):
#         return substring == substring[::-1]

# # 유사회문인지 검사하는 함수
# def psuedo(s):
#     # n = len(word)
#     # for index in range(n):
#     #     first_word = word[0:index//2]
#     #     second_word = word[index//2:]
#     #     second_word = second_word[::-1]
#     #     # 만약 끝 문자가 다르면 하나 제거하고 체크
#     #     # for word[index] != word[n-1-index]:
#     for i in range(len(s) // 2):
#         if s[i] != s[len(s) - 1 - i]:
#             # 만약 양 끝의 문자가 다르다면, 하나를 제거하고 회문인지 확인
#             modified_s1 = s[:i] + s[i + 1:]
#             modified_s2 = s[:len(s) - 1 - i] + s[len(s) - i:]

#             return is_palindrome(modified_s1) or is_palindrome(modified_s2)

#     return psuedo
            
# for i in range(t):
#     word = data[i]
#     # 회문인지 체크 -> 회문이면 check를 0으로
#     if palindrome(word)=='palindrome': 
#         check.append(0) 
#     # 유사회문인지 체크 -> 유사회문이면 check를 1로
#     elif psuedo(word) == 'psuedo':
#         check.append(1)
#     else:
#         check.append(2)

# for is_palindrome in check:
#     print(is_palindrome)
