#test4.py

# def 함수이름(매개변수):
#     실행문1
#     실행문2
#     return

# 두수를 받아서 사칙연산 출력하는 함수
def cal(a,b):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)

# 함수호출
cal(10,20)

# 점수를 받아서 합을 구해서 리턴 하는 함수 sum2(배열받는 변수)
def sum2(engli):
    sum=0
    for a in engli:
        sum=sum+a
    return

# 함수호출
eng=[90,80,70,50,60]
print(sum2(eng))

# 함수의 매개변수 *변수  - 받는 값에 따른 튜플(배열)변수
def sum_many(*a):
    # print(a)
    sum=0
    for i in a:
        sum=sum+i
    return sum

#함수호출
print(sum_many(1,2,3))
print(sum_many(1,2,3,4,5,6))
print(sum_many(1,2,3,4,5,6,7,8,9,10))

# 함수안에 매개변수에 초기값 설정
def myfun(name,old,man=True):
    print(name)
    print(old)
    print(man)
# 초기값 있으면 함수호출시 생략가능(마지막 인수만 가능)
myfun("홍길동",20,True)
myfun("이순신",30)
myfun("유관순",18,False)

# 람다 lambda  함수  : 한줄 함수
# 함수이름 = lambda 매개변수,매개변수 : 실행문
# def sum(a,b):
#     return a+b
sum=lambda a,b:a+b

print(sum(10,20))

# 람다 함수 square()  2**3  변수**변수  두수를 받아서  2의 3승 구해서 리턴
square=lambda a,b:a**b
print(square(2,3))

# mylist=[람다함수,람다함수]
# mylist=[두수를 더하는 람다함수,두수를 곱하는 람다함수]
mylist=[lambda a,b:a+b,lambda a,b:a*b];

print(mylist[0](3,4))
print(mylist[1](4,5))

# 내장함수
# map함수  
# map(람다함수,리스트자료) => 결과 리스트

# [1,2,3,4]  * 2    => [2,4,6,8]
# 함수 two_times(리스트변수)
#  리스트 변수 result=[]
#  for
#  result 리스트 값 추가 result.append(값*2)
# 리턴 result
def two_times(li):
    result = []
    for i in li:
        result.append(i*2)
    return result

print(two_times([1,2,3,4]))

# two_times2 함수 정의  하나의 값을 받아서   리턴 받은값*2
def two_times2(a):
    return a*2
# two_times3 람다 함수 정의  하나의 값을 받아서   리턴 받은값*2
two_times3=lambda a:a*2

# map(람다함수,리스트자료) => 결과 리스트
li1=list(map(two_times2,[1,2,3,4]))
li2=list(map(two_times3,[1,2,3,4]))
li3=list(map(lambda a:a*2,[1,2,3,4]))
print(li1)
print(li2)
print(li3)
# filter 함수
# filter(조건람다함수 ,리스트자료) => 함수를 통해 결과 리스트
# [1,-3,2,0,-5,6] => >0 => [1,2,6]
def pos(x):
    return x>0
# pos2 람다함수  하나의 값을 받아서  0보다 큰값 리턴
pos2=lambda x:x>0
li1=list(filter(pos,[1,-3,2,0,-5,6]))
li2=list(filter(pos2,[1,-3,2,0,-5,6]))
li3=list(filter(lambda x:x>0,[1,-3,2,0,-5,6]))
print(li1)
print(li2)
print(li3)

# 내장함수
# len()  max()  min()  type() int() abs() divmod() 몫나머지
# pow(2,3) 2의3승  range()
