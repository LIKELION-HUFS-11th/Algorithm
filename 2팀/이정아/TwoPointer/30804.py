def max_fruits(N, fruits):
    from collections import defaultdict
    
    # Initialize pointers and variables
    left = 0
    fruit_count = defaultdict(int)
    max_length = 0
    
    # Traverse the array with the right pointer
    for right in range(N):
        # Add the current fruit to the window
        fruit_count[fruits[right]] += 1
        
        # While the window has more than 2 types of fruits, shrink it from the left
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        # Update the maximum length of the window with at most 2 types of fruits
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
N = int(input())
fruits = list(map(int, input().split()))
print(max_fruits(N, fruits))

# left, right = 0, 0
# fruit_set = set()
# fruit_set.add(fruits[0])
# ans = 0

# while left <= right and right < n-1:
#     right += 1
#     fruit_set.add(fruits[right])
    
#     if len(fruit_set) > 2:
#         now_left = fruits[left]
#         while True:
#             if now_left == fruits[left+1]:
#                 left += 1
#             else:
#                 break
#         while True:
#             if now_left in fruits[left+1:right+1]:
#                 left += 1
#             else:
#                 break
#         fruit_set.discard(fruits[left])
#         left += 1
#     ans = max(ans, right-left+1)
#     # print(left, right, fruit_set)
# print(ans)