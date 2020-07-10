#0709 복습
#구조 , 함수 복습

#소스 정리르 잘해야 내가 정리 한 걸 남이 쉽게보고, 남이 정리한 걸 내가 쉽게 보기 위해서

#람다 : 익명함수

#기능적인 걸 보면 함수를 파라미터로 넘기는 경우가 있다. 
#def 라고 안주고 그냥 쓰는것 

# lambda variable_define : statments

def add(a,b):
    return a+b

print(add(10,20))

add2 = lambda a, b : a+b

print(add2(10,20))

# 호출 한 번 필요한 경우만 쓰면 된다. 흐름방해시?


div = lambda a, b : a/b

def cal(func, a, b):
    return func(a,b)


cal(div, 1, 2)
cal(add2, 1, 2)


#작은 프로젝트에 대한, 요청에 대한 빠른 반응을 코드짤 떄

#모듈
#따로관리하면 좋지 않을까

#파이썬 파일이다.

#2교시



import exam_module as em

print(em.myadd(4,5))


#경로 어디에 있는지가 중요하다. 실행위치의 기준으로 모듈파일이 어디있는가. 
#모듈을 디렉터리 별로 관리하는 것. 그걸 모아놓은것을 패키지!!


#많은 모듈이 있을 때, 찾기 쉽도록 할 수 있다. 

# from 패키지 경로 import 모듈 as 식별자
# 모듈을 as로 정의 할 때, 보통적으로 많이 쓰는 네임이 있긴하다.

#모듈화 할 때 입력기능 출력기능을 일단 기본적으로 나누고
#회사가서 기준에 맞추면 된다. 스탠다드가 있긴한데, , 잘안따른다.




import pickle as p

#파일 입출력 쉽다.

# open 함수 스면된다. open(파일이름, 모드, 인코딩)

f = open("exam14.txt", "w")
f.write("abc\n")
f.close()

abc = [1,2,3,4,5,6,7,8,9]
# 피클을 많이 쓴다.

def pw():
    f = open("exam14.txt", "wb")
    p.dump(abc, f)
    f.close()

    #메모리의 기록을 그대로 파일로 저장한다해서 dump 라고 한다. 



#파일에 담겨있는 정보를 딕셔너리 형태로 가져오는 것.?

















