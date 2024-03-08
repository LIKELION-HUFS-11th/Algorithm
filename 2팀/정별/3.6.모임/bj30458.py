def main():
    len_s = int(input())
    s = input()
    cnt = [0] * 26

    for char in s: #각 알파벳의 등장횟수 저장
        cnt[ord(char) - ord('a')] += 1

    if len_s % 2 == 1: #홀수면 중간 문자는 굳이 짝 이룰 필요없으니 등장횟수줄임
        cnt[ord(s[len_s // 2]) - ord('a')] -= 1

    for frequency in cnt: #홀수번 등장하는 알파벳있으면 팰린드롬으로 만들 수 없음
        if frequency % 2 == 1:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()



# def is_palindrome_possible(N, S):
#     left_half = S[:N//2]
#     right_half = S[N//2 + N % 2:]

#     reversed_left_half = left_half[::-1]

#     # 왼쪽 절반과 오른쪽 절반 비교
#     differences = [i for i in range(len(left_half)) if left_half[i] != right_half[i-len(left_half)]]

#     if not differences:
#         return "Yes"

#     for diff_index in differences:
#         if left_half[diff_index] == right_half[diff_index - len(left_half)]:
#             return "Yes"

#     return "No"

# N = int(input())
# S = input()

# print(is_palindrome_possible(N, S))
