# def solve(n):
#   """
#   현석이를 만족시키면서 정수 1, 2, ..., N을 선물하는 방법을 찾습니다.

#   Args:
#     n: 정수의 개수 (1 < N < 5000)

#   Returns:
#     (성공 여부, 선물 순서)
#   """

#   # 1부터 N까지의 합
#   Sn = n*(1+n)//2

#   # Miller-Rabin 소수 판별법
#   def is_prime(n):
#     if n <= 1:
#       return False

#     if n <= 3:
#       return True

#     if n % 2 == 0 or n % 3 == 0:
#       return False

#     i = 5
#     while i * i <= n:
#       if n % i == 0 or n % (i + 2) == 0:
#         return False
#       i += 6

#     return True

#   # 선물 순서를 저장할 리스트
#   order = []

#   # 1부터 N까지의 정수를 리스트에 저장합니다.
#   numbers = list(range(1, n + 1))

#   # 리스트가 비어질 때까지 반복합니다.
#   while numbers:
#     # 리스트의 첫 번째 수를 제거하고 현석이에게 선물합니다.
#     order.append(numbers.pop(0))

#     # 리스트의 다음 수를 선택합니다.
#     next_number = None
#     for number in numbers:
#       if not is_prime(number):
#         if next_number is None or number > next_number:
#           next_number = number

#     # 리스트에서 다음 선물 번호를 제거합니다.
#     if next_number is not None:
#       numbers.remove(next_number)

#   # 현석이를 만족시키면서 선물하는 방법이 있다면 "YES"를, 그렇지 않다면 "NO"를 출력합니다.
#   if len(order) == n:
#     return "YES", order
#   else:
#     return "NO", []

# # 입력
# n = int(input())

# # 출력
# success, order = solve(n)
# print(success)
# if success == "YES":
#   print(" ".join(map(str, order)))



