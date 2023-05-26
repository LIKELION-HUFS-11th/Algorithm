def recursive_function(): #이 함수에 대해 정의해줄게
    print('재귀 함수를 호출합니다.') #해당 문자열을 출력하고 자기 자신을 또 호출하는 함수야
    recursive_function() 

recursive_function() #이 함수를 호출하자

#결국 해당 문자열이 무한히 반복될 것

