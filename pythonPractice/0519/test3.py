#다중상속

# # 다중상속

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


l=Liger()  #자식클래스 생성

l.play()
l.bite() # 재정의 안했기 때문 부모것 쓺. 
l.jump()

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

c1=Car("빨강")   #객체생성

print(c1.color)
print(c1.count)
print(Car.count)
c1.move()

c2=Car("노란")
print(c2.color)
print(c2.count)
print(Car.count)
c2.move()


#test6(쌤파일) 예외처리 p222 무슨 시수4번만에 220페이지,, 
# 다시 생코로 들어야 할 듯. 그래서 뭘 만들 수 있는데??

# 모듈 패키지를 외부에서 가져다 쓰면서,  다양한게 많은데

# 데이터 분석, 시각화, 등등 을 할수 있다.







#예외처리

print("프로그램 시작")

a=4
b=2

if b!=0:
    print(a/b)

else:
    print("0으로 나눔")

print("프로그램 끝")

# 왜 결과가 2.0으로 나타나지?

print("프로그래 시작1")
try:
    #예외발생구문
    print(a/b)
except ZeroDivisionError as e:
    print(e)
finally:
    print("예외발생 상관없이 마무리 작업")
print("프로그램 끝2")


#배열 범위를 넘어갔을 때


a = [1,2,3]

try:
    print(a[3])

except IndexError as e:
    print(e)

finally:
    print("생략가능")

# 오류발생 -> 회피(오류메시지 없이 그냥 지나침) pass
try:
    f=open("없는파일",'r')
except FileNotFoundError as e:
    # print(e)
    #예외 회피
    pass
finally:
    print("생략가능")


# 오류 일부러 발생

class Bird:
    def fly(self):
        raise NotImplementedError
b=Bird()
b.fly()


# 메서드 재정의 하면 오류 없어짐

# 이 과정을 그냥, 이런식으로 무식하게 배우면 안된다는걸
#느끼는 과정으로 생각하자. 어차피 배움에 있어선 한가지 길이아니다.
#무식하게 배우다가도 효율적 방법을 찾을 수있고
# 효율적이라고 했는데 그 과정을 몰라서 다시 무식하게 갈수도있는 것.
# 

class Eagle(Bird):
    def fly(self):
        print("메서드 오버라이딩")

e=Eagle()
e.fly()


