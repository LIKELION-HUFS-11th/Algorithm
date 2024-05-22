import sys

nList = list(sys.stdin.readline())

nNums = ['1','2','3','4','5','6','7','8','9']
nExp = [] #계산할 최종식

Flag = False #괄호 열려있으면 True

for elem in nList: #어차피 식 길이는 50이하임.
    if elem in nNums or isinstance(elem, int): #처음이나 마지막은 정수
        nExp.append(int(elem))        
    else: # +나 -라면
        if elem == '-':
            if not Flag: #괄호 닫혀있는 상태
                nExp.append('-').append('(')
                Flag = True
            else: #괄호 열려 있으면
                nExp.append(')')
                
                append('-')
        
        else: #'+' 일때
            nExp.append('+')
            
                
 
        