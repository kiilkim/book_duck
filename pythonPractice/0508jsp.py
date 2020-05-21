#test2.py
#  제어문  조건 


#true 와 false 가 나와야 한다.

# 참 True 거짓 False  boolean  형
# 

a=80

if a >= 60:
    print("pass")

else:
    print("reTest")


x=3
y=2

x>y


# json 데이터를 리스트 딕셔너리라는 자료형으로 쉽게 관리한다.


# 조건    숫자 0이면 False      0아니면 True
#        문자열 ""이면 False    ""아니면 True
#        리스트 []이면 False    []아니면 True
#        튜플  ()이면 False     () 아니면 True
#        딕셔너리 {}이면 False   {} 아니면 True

# 카드가 있으면 "택시타라"  없으면 "걸어가라"
card=3
if card:
    print("택시타라")
else:
    print("걸어가라")



# 논리연산자  and or
# 놀이기구 키가 155이하 이고 몸무게 50이하 "입장가능" 아니면 "입장불가능"
h=165
w=60
if h<=155 and w<=50:
    print("입장가능")
else:
    print("입장불가능")



# 주민번호에서 성별코드가 "1"이거나 "3"이면 "남" 
#    아니면 "여"
j="9001223-1234567"

#j 변수의 9번째 자리가 1 or 3 이면 : >어떻게 표현하지

# 남
#else:
#여

if j[7] == "1" or j[7] =="3" :
    print("남")

else: 
     print("여")

# if 조건1:
#     조건1True 실행문
# elif 조건2:
#     조건1False 조건2True 실행문
# else:
#     False 나머지 실행문

# 양수, 0, 음수  출력
a=-5
a=-5
if a>0:
    print("양수")
elif a==0:
    print("0")
else:
    print("음수")

#list 자료형 ----[] 로 표현 . 배열이랑 비슷하다.
# 외부에서 자료를 가져올때, 리스트형, 등으로 자료분석하기 쉽도록


#많이 쓰낟. 
#json 에서 


a = [1,3,5,7,9]
b = []

c= ['a','b','c', 1,2,3] 

#문자 숫자 같이 들어갈 수 있다.

print(a)
print(a[0])
print(a[-1])
print(a[0]+a[-1])
print(a[0:2])
print(a[:2])
print(a[2:])
print(len(a))
print(type(a)) #<class 'list'>

print(a*3) #반복
print(a+c)

# 수정,변경 삭제
print(a)  #[1, 3, 5, 7, 9]
a[2]=4
print(a) #[1, 3, 4, 7, 9]
print(a[1:2])
a[1:2]=['a','b','c']
print(a)
a[1:3]=[]
print(a)
del(a[1])
print(a)

#리스트 함수
a=[1,2,3]
#추가
a.append(4)  #[1, 2, 3, 4]
print(a)
#삽입
a.insert(0,0)
print(a)  #[0, 1, 2, 3, 4]
#제거
a.remove(0)
print(a) #[1, 2, 3, 4]
#뒤집기
a.reverse()
print(a) #[4, 3, 2, 1]
# 정렬
a.sort()
print(a) #[1, 2, 3, 4]



# 값 in 리스트  / 값  not  in 리스트
# 리스트에 찾는값이 있으면 True 없으면 False
a=[1,2,3,4]
print(1 in a)  #True

p=['paper','phone','money']
# p에서 'money'있으면 "택시타라"   없으면 "걸어가라"

if print("money" in p):
    print("택시타라")

else:
    print("걸어가라")


if 'money' in p:
    print("택시타라")
else:
    print("걸어가라")

# 튜플 => 값수정 못하는 리스트   ()
t1=()
t2=(1,)
t3=(1,2,3)

# t3[0]=0  # 값변경 못함


# 딕셔너리

# 튜플 => 값수정 못하는 리스트   ()
#고정된 리스트 사용시


t1=()
t2=(1,)
t3=(1,2,3)

# t3[0]=0  # 값변경 못함
# del(t3[0]) # 값삭제 못함



# 딕셔너리

t=(1,2,'a','b')
print(t[0]) #1
print(t[1:])  #(2, 'a', 'b')

print(t+t3)  #(1, 2, 'a', 'b', 1, 2, 3)
print(t*3)


# 딕셔너리
#순서가 없고 키 : 값 임


# {"키":"값","키":"값"}
d={'id':'kim','name':'kimgildong'}
print(d)
# d[키]=값
d['birth']='1225'
print(d)  #{'id': 'kim', 'name': 'kimgildong', 'birth': '1225'}
#추가
d[1]='a'
print(d) #{'id': 'kim', 'name': 'kimgildong', 'birth': '1225', 1: 'a'}
#삭제
del(d[1])
print(d) #{'id': 'kim', 'name': 'kimgildong', 'birth': '1225'}


# 키값 가져오기
print(d.keys())  #dict_keys(['id', 'name', 'birth'])
#리스트 변경
li=list(d.keys())
print(li)  #  ['id', 'name', 'birth']
#값 가져오기
print(d.values()) #dict_values(['kim', 'kimgildong', '1225'])
# 키, 값 가져오기
print(d.items())
#dict_items([('id', 'kim'), ('name', 'kimgildong'), ('birth', '1225')])
# 키에 해당하는 값 가져오기
print(d.get('id'))  #kim

#전체삭제
d.clear()
print(d)  #{}


# 집합자료형   set  순서없음  중복 허용하지 않음
s1=set([1,2,3])
print(s1)  #{1, 2, 3}

s2=set("Hello")
print(s2)  #{'l', 'o', 'H', 'e'}

l=list(s1)
print(l)  #[1, 2, 3]
t=tuple(s1)
print(t)  #(1, 2, 3)

# 차집합, 교집합, 합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
# 교집합
print(s1&s2)                   #{4, 5, 6}
print(s1.intersection((s2)))   #{4, 5, 6}
#합집합
print(s1|s2)                   #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))            #{1, 2, 3, 4, 5, 6, 7, 8, 9}
#차집합
print(s1-s2)                   #{1, 2, 3}
print(s1.difference(s2))       #{1, 2, 3}

#모든 형은 참조형이다.

a=10
a=3.4
a="hello"
a=[1,2,3]
a=(1,2,3)
a={1:'a',2:'b'}
a=set([7,8,9])


a=3
b=3
c=3
print(id(a))
print(id(b))
print(id(c))


#a 주소 값이 있는데 3을 가리킴
# b 주소값이 같다면 3을 가리킴, 뭐의 절약/ 



a,b=10,20
a,b=('a','b')
print(a)
print(b)
(a,b)='c','d'
[a,b]=['e','f']
a=b='p'



#두수교환
a=10
b=20
a,b=b,a
print(a)
print(b)

# 메모리 변수 삭제
a=3
b=3
del(a)
# print(a)

a=[1,2,3]
b=a
a[1]=4
print(a) #[1, 4, 3]
print(b) #[1, 4, 3]


#docstring 뭔가 난잡한 글을 표현 할떄? 아니 그 pre 같은느낌이네

print('''
H
e
l
l
o
''')


a=[1,2,3]
b=a[:] #값 주소를 복사하다. 값은 같이 사용 한다. 
a[1]=4
print(a) #[1, 4, 3]
print(b) #[1, 2, 3]

