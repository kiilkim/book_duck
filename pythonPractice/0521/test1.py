#모듈 207p(test8 T)

#모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일
# 이미 만들어진 모듈을 만들 수도 있다. 


def sum(a,b):



    return a+b

# cmd
# d:
# D:\workspace_py\py1
# dir
# python


#쓰고 sum 함수쓰기 

# print(sum(10,20))   => 에러발생
# import test8   => test8.py 가져오기
# print(test8.sum(10,20))   => test8에 있는 sum함수 호출


# safe_sum() 함수 정의 두수를 받아서 ok
#  type()  타입이 틀리면  "더할수 없는 데이터입니다" 리턴
#                같으면  더해서 리턴

# java는 문자숫자 연결되는데 파이썬은 에러난다.
# 

def safe_sum(a,b):
    
    if type(a) != type(b):


        result = print("더할수 없는 데이터타입입니다.")

        return a+b

print(safe_sum(10,20))


def safe_sum(a,b):
    if type(a) != type(b):
        return "더할수 없는 데이터입니다"
    else:
        return sum(a,b)

# from 모듈이름(파일이름) import 함수이름
# from test8 import sum
# print(sum(10,20))

# from test8 import sum,safe_sum
# from test8 import *
# print(sum(10,20))
# print(safe_sum(10,20))

# import test8 as t8
# print(t8.sum(10,20))
# print(t8.safe_sum(10,20))

#외부의 패키지 파일 등 가져올 때도 모듈에서 가져오는거라서, ,

# Math 클래스 solv() 원면적 함수
PI=3.141592
class Math:
    def solv(self,r):
        return PI*(r**2)

print(PI)
# 객체생성

m=Math()  #함수로 객체생성이 아닌,,class 객체생성



# solv() 함수 호출

print(m.solv(10))
print(sum(10,20))
print(safe_sum('a',1))



