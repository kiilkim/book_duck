# test5.py
# 클래스 정의 (사물,객체,업무...) 특징 저장하는 변수, 특징을 처리하는 기능(함수)

# class 클래스이름:
#     주제 변수1
#     주제 변수2
#     주제 처리 함수1
#     주제 처리 함수2

# 객체생성
# 변수 = 클래스이름()

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

# 초기값 설정
class Person:
    #초기값 함수(클래스 안에 있는 내장함수)
    def __init__(self,name,age):
        # self.name 인스턴스 멤버변수
        self.name=name
        self.age=age
    def intro(self):
        print("이름",self.name,"나이",self.age)

p=Person("홍길동",20)
p.intro()

# 클래스 FourCal2   초기값 a,b 받아서  sum함수 a,b 더한값 리턴
#                  sub함수 a,b 뺀값 리턴 , mul함수 a,b 곱한값 리턴
#                  div함수 a,b 나눈값 리턴

# 객체 생성 메서드 호출
class FourCal2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

f2=FourCal2(10,20)
print(f2.sum())
print(f2.sub())
print(f2.mul())
print(f2.div())

# 클래스 상속
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
        print(self.color,"자전거 접기")
# FoldingBicycle 객체생성
# move()  fold() 함수 호출
f=FoldingBicycle("노란색")
f.move(30)
f.fold()

# 부모클래스 안에 내장 함수 __add__          __sub__
#       부모클래스+자식클래스 (add함수호출)   부모클래스-자식클래스(sub함수호출)

# 부모클래스 HousePark
#  멤버변수 lastname="박"
# 초기값 name 받아서 self.fullname= self.lastname+name
# 함수정의 travel(where) 출력   self.fullname 이 where 여행가다
class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print(self.fullname,"이",where,"여행가다")
    def __add__(self, other):
        print(self.fullname,"와",other.fullname,"여행지에서 만나다")
    def __sub__(self, other):
        print(self.fullname, "와", other.fullname, "여행지에서 헤어짐")
# 자식클래스 HouseKim 상속 HousePark
#  멤버변수 lastname="김"
# 함수 재정의 travel(where,day) 출력 self.fullname 이 where에 day일 여행가다
class HouseKim(HousePark):
    lastname = "김"
    def travel(self,where,day):
        # 부모메서드 호출
        super().travel("강원도")
        print(self.fullname,"이",where,"에",day,"일 여행가다")

# 부모클래스 HousePark 객체생성
p=HousePark("순신")
# HouseKim 객체생성
# travel() 함수 호출
h=HouseKim("길동")
h.travel("제주도",10)

# __add__ 함수 호출
p+h
# __sub__ 함수 호출
p-h

# 다중상속
class Tiger:
    def jump(self):
        print("호랑이 점프")
class Lion:
    def bite(self):
        print("사자 꿀꺽")

class Liger(Tiger,Lion):
    def play(self):
        print("라이거 놀기")
    def jump(self):
        print("라이거 점프")

l=Liger()
l.jump()
l.play()
l.bite()

# 인스턴스 self.변수 인스턴스 함수(self)
# 객체생성없이 사용할수 있는 클래스변수, 클래스 함수
class Car:
    count=0
    def __init__(self,color):
        self.color=color
        # 클래스 변수 : 객체생성없이 사용하는 변수, 클래스 정의때 기억장소 할당
        Car.count=Car.count+1
    # 인스턴스 함수 
    def move(self):
        print(self.color,"차가 움직인다")
    # 스태틱 함수
    @staticmethod
    def check():
        print("static 함수")
    # 클래스 함수
    @classmethod
    def check2(cls):
        #클래스 변수 사용
        print(Car.count,"클래스 메서드")

#스태틱함수 호출
Car.check()
# 클래스 함수 호출
Car.check2()

c1=Car("빨강")
print(c1.color)   #   인스턴스 변수 : 객체생성시 기억장소 할당
print(c1.count)  #1   클래스 변수 : 클래스 정의때 기억장소 할당
print(Car.count)
c1.move()
# Car.move() 에러
c2=Car("노란")
print(c2.color)
print(c2.count)  #2
print(Car.count)
c2.move()


