#1교시

#복습
#한줄함수

##
#def = define 정의한다 는뜻

# def 함수이름(매개변수): 후 엔터쳐서 tab만클
# (tab)실행문  
#      return

def first():
    print("함수다")

#두 수를 받아서 사친연산 출력함수

def cal(a,b):
    return a+b

a=10
b=20


print(cal(a,b))

    
c= cal(a,b)

print(c)


#입력값이 없는 함수



# 두수를 받아서 사칙연산 출력하는 함수
def cal(a,b):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)

# 함수호출
cal(10,20)

eng=[90,80,70,50,60] #영어점수

#점수를 받아서 // 어떻게 받지??

sum = 0

for i in eng:  #i에 eng 배열의 값을 배정한다 는 맞는데. 
    sum +=i

    print(sum)

def calSum():
    return sum

s = calSum()

print(s)



def add(a,b):
    return a+b

result = add(a=3, b=4)

print(result)


result = add(a=5 ,b =7)

print(result)


#입력값이 몇개일지 모를 때


def add_many(*args):
    result = 0

    for i in args:
        result +=i

    return result


result = add_many(1,2,3,8)
print(result)

# 개인의 어항이 몇개일지 모르니, 어항의 온도는 개인의 어항 갯수에 따라다름
# 

# 함수안에 매개변수에 초기값 설정
def myfun(name,old,man=True):
    print(name)
    print(old)
    print(man)
# 초기값 있으면 함수호출시 생략가능(마지막 인수)
myfun("홍길동",20,True)
myfun("이순신",30)
myfun("유관순",18,False)


# 람다 lambda  함수  : 한줄 함수
# 함수이름 = lambda 매개변수,매개변수 : 실행문

# 한줄에 함수 표현
# def sum(a,b):
#     return a+b


#함수가 복잡하지 않게 여러개 할 수 있는 것.
#무조건 짧게, 등 위함. 앞으로 메모리의 향상 덕분에
# 메모리 차지하는 것 관련없는 언어가 더 뜨것이다.
# c,java 당시에는 메모리 걱정이 있었다 (java는 나아졌지만서도)
# 지금은 얼마든지 적은 폰 기기에 , 태블릿에 성능좋은 메모리 탑재 가능)
# 

sum=lambda a,b:a+b

print(sum(10,20))


square=lambda a,b : a**b

print(square(2,15))

mylist=[lambda a,b:a+b,lambda a,b:a*b]

print(mylist[0](3,4))
print(mylist[1](4,5))


#내장함수
# map 함수
# filter 함수


# [1,2,3,4]  * 2    => [2,4,6,8]
# 함수 two_times(리스트변수)
#  리스트 변수 result=[]
#  for  리스트 값 추가 append(값*2)
# 



def two_times(li):
    result = []
    for i in li:
        result.append(i*2)
    return result

print(two_times([1,2,3,4]))

# two_times2 함수 정의  하나의 값을 받아서 리턴*2
# 배열상관없이. 하나의 값.. 
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

#대량의 데이터를 가져와서 작업할 때 유리하다.



# filter 함수

# 안에서도 lambda사용 가능
# 리스트중 0보다 큰 값만 찾아내는 것. 
# [1,-3,2,0,-5,6] => >0 => [1,2,6]

def pos(x):
    return x>0

#람다함수 만들기
pos2 = list(map(lambda a : a>0,[-1,-2,3,4,5]))

print(pos2)


pos3=lambda x: x>0

lis=list(filter(pos,[-1,-2,3,4]))

print(lis)

#어항 4개가 있는데 4개중 온도가 28도 넘은것 걸러내기
#-> 걸러내서 온도조정->조정할 온도계에 신호주기

