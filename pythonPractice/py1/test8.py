#test8.py
# p207
# 모듈 : 변수,함수,클래스 모아놓은 파일
# 패키지 : 모듈을 모아서 저장하는 폴더

# sum() 두수를 받아서 합을 구해서 리턴
def sum(a,b):
    return a+b

# cmd
# d:
# cd D:\workspace_py\py1
# dir
# python
# print(sum(10,20))   => 에러발생
# import test8   => test8.py 가져오기
# print(test8.sum(10,20))   => test8에 있는 sum함수 호출

# safe_sum() 함수 정의 두수를 받아서
#  type()  타입이 틀리면  "더할수 없는 데이터입니다" 리턴
#                같으면  더해서 리턴
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

# Math 클래스 solv() 원면적 함수
PI=3.141592
class Math:
    def solv(self,r):
        return PI*(r**2)

# 테스트용으로 파일 실행할때 동작
# import 할때는 동작 안됨
if __name__=="__main__":
    print(PI)
    # 객체생성
    m=Math()
    # solv() 함수 호출
    print(m.solv(10))
    print(sum(10,20))
    print(safe_sum('a',1))