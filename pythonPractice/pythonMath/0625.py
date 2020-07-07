#연습문제.
#1. 숫자를 받으면 몇째자리 수인지 돌려주는 코딩함수


def indexNum(a):

    return len(str(a))

print(indexNum(1234))


#2. 숫자를 받으면 공통된 숫자를 출력하라
# 근데 공통 숫자를 출력하는게 아니라, 문자다.
# 숫자를 받는건 함수(숫자,숫자)로 되는데 
# 그 받은 숫자를 숫자로 인식하고 공통의 수를 찾아내야한다.

#숫자에 인덱스가부여되나? no 다만 정수형 자료는 index로 접근할 수 없습니다.


a = '12345'

print(a[0])

def sameNum(a,b):
    c=[]

    for i in str(a):
        if i in str(b):
            
            c.append(int(i))
    
    return c

print(sameNum(38472,173))

    
# 3. 두집합의 차집합으로 이루어진 함수를 교집합,차집합으로부터구하여라
#(a−b)∪(b−a)  

# 전체 - 교집합

# 두집합의 차집합을 구해보자

def complement(a,b):

    c = a + []
    
    for i in b:
        if i in a:
            c.remove(i)

    return c

    
a=[1,2,3]
b=[3,4,5]

print(complement(a,b)+complement(b,a))


# a,b,c 세집합이 잇을때 세집합의 교집합과 각집합에만 해당하는 부분만
# a,b,c 모두 공통인 부분 구하기, 교집합, 그리고, 
# a-b-c 와 b-c-a 그리고 c-a-b의 값을 구하고 더하기

def intersection(a,b):
    c= []
    for i in a:
        if i in b:
            c.append(i)
    return c

def complement(a,b):
    
    c = a + []
    for i in b:
        if i in a:
            c.remove(i)
    return c

def complementDouble(*lists):

    d = complement(lists[0],lists[1])

    for i in lists[2:]:
        d = complement(d,i)
        d.sort()
    
    return d





def tripleCircle(*lists):

    d = intersection(lists[0],lists[1])


    for i in lists[2:]:
        d = tripleCircle(d,i)
        d.sort()
      

    return d

a=[1,3,5,7,9]

b=[1,3,4,8,10]

c=[1,3,5,2,4]

print(tripleCircle(a,b,c))

print(complementDouble(a,b,c))
print(complementDouble(b,c,a))
print(complementDouble(c,a,b))

print()
    

# A가 B의 부분집합인지? 
# A가 B에 다 포함되어 있어야 부분집합이라고 한다.
# A의 원소가 모두 B에 포함되어 있어야 한다.
def part(a,b):

    c = []
    for i in a:
        if i in b:
            c.append(i)
            print('true')

        elif i not in b:
            print('false')
    return c

a=[1,2,5]
b=[1,2,3,4]
print(part(a,b))

# 다 true 가 아니기 때문에 a는 b의 부분집합이 아니다.
# 다 true 이기 때문에 a는 b의 부분 집합이다.


# 8. 50명중 20명은 A하키 15명은 B야구 11명은 C축구
# AnB 는 7 BnC 는 4 CnA는 5
# 아무것도 안하는 Uc는 18명 , 
# 2개의 스포츠만 하는 학생은? 


# 7~11번까지 잘 모르겠당.


def union(a,b):
    
    c =[]

    for i in a:
        if i not in b:
            c.append(i)
    
    c = c + b
    c.sort() 

    return c




a=[1,2,7,15,23]
b=[2,15,16,27]

print(union(a,b))
print(intersection(a,b))

#파트 2 자연수, 정수,유리수, 무리수

# 

a=5
a>10

print(a>10)

# 사실은 if 다음에 bool 자료형이 온다는 사실

for i in [1,2,3,4,5]:
    if i > 3 :
        print(i)


def odd_or_even(n):
    if n % 2 == 0:
        print('{}은 짝수이다'.format(n))
        k='even'
    elif n % 2 !=0:
        print('{}은 홀수이다'.format(n))
        k='odd'
    return n

print(odd_or_even(9))
print(odd_or_even(4))

# 숫자의 자료형과 그 연산

# 정수형 소수형 자료형은 연산과정에서 에러가
# 발생하지 않는다.

# 다만 정수형+소수형 자료면 소수형이 된다.

# 거듭제곱은 m**n 이다

# (-2)**2 와 -2**2는 다르다. 왜?

# 제곱근을 위해선 넘파이를 쓴다. 


a = range(5)

for i in range(5):
    print(i)

    #range(5)와 range(0,5)는 같은 의미
# 1~n 까지의 합

a = 0

for i in range(0,101):
    a+=i

print('0부터100까지 더한 값: {}'.format(a))

# enumerate 원소의 순서와 값, 2개를 동시에 돌려주는 기능

fruit = ['strawberry', 'grape', 'apple', 'mango', 'orange']
a = list(enumerate(fruit))

print(a)


a=10
c=0

while a>0:
    c+=a
    a-=1

print(c)

a = True
n = 0

while a:
    n+=1
    print(n)
    if n == 20:
        a=False
















