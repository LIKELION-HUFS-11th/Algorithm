import sys
string = sys.stdin.readline()
cr_list_two = ['lj','nj']
cr_list_one = ['c=', 'c-','d-', 's=','z=']

result = 0
left= 0
right=2
while right<len(string):
    print(string[left:right])
    if right < len(string)-1 and string[left:right+1]=="dz=":
        left +=3
        right +=3
        result +=1
    elif string[left:right] in cr_list_two:
        left += 2
        right += 2 
        result+=1
    elif string[left:right] in cr_list_one:
        left +=2
        right+=2
        result+=1
    else:
        left += 1
        right +=1
        result+=1

print(result)

