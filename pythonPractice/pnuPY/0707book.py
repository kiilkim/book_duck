#자료형 변수와입력

pi=3.14159265

r = 10 

print("원주율 = ",pi)

print("반지름 =",r)

print("원의둘레 =",2*pi*r)


# 변수형을 설정안해줘서 좋긴 하지만, 팀프로젝트 할 떄 서로 충돌할 가능성


#복합 대입연산자

r +=10

print(r)


#빼기, 곱하기, 나누기, 몫 등 에 제곱도 가능 '연산 후 대입!'
#문자열도 가능하다.


string = input("입력 >")

print("자료 :",string) 



#090 문제 5

str_input = input("원의반지름입력>")
num_input = int(str_input)

print("반지름:",num_input)

print("둘레:",2*3.14*num_input)

print("넓이:",3.14*num_input**2)

#format 함수로 숫자를 문자열로 반복

string_a ="{}".format(10)

print(string_a)

print(type(string_a))















