#재귀적으로 팩토리얼을 어떻게 구현

def factorial_recursive(n):
    if n <=1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5))


