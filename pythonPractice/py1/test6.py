# test6.py

# 예외처리 
print("프로그램 시작")
a=4
b=0
if b!=0:
    print(a/b)
else:
    print("0으로 나눔")
print("프로그램 끝")

print("프로그래 시작1")
try:
    #예외발생구문
    print(a/b)
except ZeroDivisionError as e:
    print(e)
finally:
    print("예외발생 상관없이 마무리 작업")
print("프로그램 끝2")

a=[1,2,3]
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
# b=Bird()
# b.fly()

# 메서드 재정의 하면  => 오류 없어짐
class Eagle(Bird):
    def fly(self):
        print("fly() 메서드 오버라이딩")
e=Eagle()
e.fly()



