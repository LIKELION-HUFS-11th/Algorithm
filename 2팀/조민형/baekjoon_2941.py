import sys
string = sys.stdin.readline()
cr_list_one = ['c=', 'c-','d-', 's=','z=','lj','nj']

result = 0
left= 0
right=1
while right<len(string):
    if right < len(string)-2 and string[left:right+2]=="dz=":
        left +=3
        right +=3
        result +=1
    elif right < len(string)-1 and string[left:right+1] in cr_list_one:
        left +=2
        right+=2
        result+=1
    else:
        left += 1
        right+=1
        result+=1

print(result)

