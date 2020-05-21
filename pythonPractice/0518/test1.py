#지난시간 복습 

#람다 함수 한줄에 표현하고 싶을 때
#함수이름 = lambda 매개변수, 매개변수 : 실행문

#1교시

#클래스 183p
# 클래스 정의 (사물,객체,업무...) 특징 저장하는 변수, 특징을 처리하는 기능(함수)

# class 클래스이름:
#     주제 변수1
#     주제 변수2
#     주제 처리 함수1
#     주제 처리 함수2


result = 0

def add(num):
    global result
    result +=num
    return result

print(add(3))
print(add(4))


class Simple:
    # pass
    s="변수"
    def prn(self):
        print("함수정의")
    def sum2(self,a,b):
        return a+b

a=Simple()
print(a.s)
a.prn()
print(a.sum2(10,20))


#초기값 설정

class Person:
    #초기값 함수(클래스 안에 있는 내장함수)
    def __init__(self,name,age):
        # self.name 인스턴스 멤버변수
        self.name=name
        self.age=age
    def intro(self):
        print("이름",self.name,"나이",self.age)


p=Person("홍" ,20)
p.intro()

# 클래스 FourCal2   초기값 a,b 받아서  sum함수 a,b 더한값 리턴
#                  sub함수 a,b 뺀값 리턴 , mul함수 a,b 곱한값 리턴
#                  div함수 a,b 나눈값 리턴

# 객체 생성 메서드 호출



class fourCal2:

    def __init__(self, a,b):

        self.a=a  #멤버변수에 담는다. 
        self.b=b
    #각 함수 정의 return값 설정 
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

p=fourCal2(20,30)
print(p.sum())
print(p.sub())
print(p.mul())
print(p.div())

#사칙연산 클래스 만들기

class FourCal:

#객체에 숫자 지정
#a에 사칙연산할 숫자 알려주기 
    #setdata 함수 만들기
    #매서드라고 표현
    def setdata(self, first, second): #매개변수
        self.first = first   #매서드 수행문
        self.second = second
#self의 의미

    def add(self):
        result = self.first + self.second
        return result

a = FourCal()

a.setdata(4,2)

print(a.add())


#클래스 상속

class Parent:
    def parent_prn(self):
        print("부모클래스 prn()함수")

class Child(Parent): #Parent 상속
    def child_prn(self):
        print("자식클래스 prn()함수")
    #메서드 오버라이딩 : 부모메서드 재정의
    def parent_prn(self):
        print("자식클래스가 재정의한 부모클래스 prn()함수")

# Child 객체생성    parent_prn()     child_prn() 메서드 호출
c=Child()
c.parent_prn()
c.child_prn()


# Bicycle 클래스
# 초기값 color 받아 멤버변수 color 변수에 저장
#  move(speed) 함수   출력   color , 자전거 속도 speed
class Bicycle:
    def __init__(self,color):
        self.color=color
    def move(self,speed):
        print(self.color,"자전거 속도",speed)

# FoldingBicycle 클래스  상속 Bicycle
# fold()함수  출력 color "자전거 접기"
class FoldingBicycle(Bicycle):
    def fold(self):
        print(self.color,"자전가 접기")

# FoldingBicycle 객체생성
# move()  fold() 함수 호출



f = FoldingBicycle("노란색")

f.fold()
f.move(30)
# 부모클래스 안에 내장 함수 __add__          __sub__
#       부모클래스+자식클래스 (add함수호출)   부모클래스-자식클래스(sub함수호출)

# 부모클래스 HousePark
#  멤버변수 lastname="박"
# 초기값 name 받아서 self.fullname= self.lastname+name
# 함수정의 travel(where) 출력   self.fullname 이 where 여행가다

# 자식클래스 HouseKim 상속 HousePark
#  멤버변수 lastname="김"
# 함수 재정의 travel(where,day)   출력   self.fullname 이 where에 day일 여행가다

class HousePark:

    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
        
    def travel(self,where):
        print(self.fullname,"이",where,"여행가다")



