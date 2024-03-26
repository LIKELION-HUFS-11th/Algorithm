import sys
input = sys.stdin.readline

cases = int(input())

for i in range(cases):
    n, m = list(map(int, input().split()))  
    nums = list(map(int, input().split()))  

    ans = 1
    while nums:
        if nums[0] < max(nums):
            nums.append(nums.pop(0))    
        
        else:
            if m == 0:
                break

            nums.pop(0)
            ans += 1
        
        if m > 0:
            m = m - 1 
        else:
            m = len(nums) - 1
    
    print(ans)