import sys
T = int(sys.stdin.readline())

def fibonacci(n) :
        fibonacci_list = [0] * (n+1)
        fibonacci_list[0] = 0
        fibonacci_list[1] = 1
        for i in range(2,n+1):
            fibonacci_list[i] = fibonacci_list[i-1] + fibonacci_list[i-2]
        return fibonacci_list 
    
    
result = []
for i in range(T):
    case = int(sys.stdin.readline())
    if case == 0:
         result.append("1 0")
    elif case==1:
        result.append("0 1")
    else:
        fibonacci_listed = fibonacci(case)
        result.append(f"{fibonacci_listed[case-1]} {fibonacci_listed[case]}")

for j in result:
    print(j)
    


    
