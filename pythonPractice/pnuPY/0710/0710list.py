#숫자모음 등을 모아주는 것._리스트

list = [1,3,5,7,9] #가장 간단. 
#리스트명=[요소1,요소2,요소3,,,] "문자", 숫자

#리스트 자체를 요소로도 가질 수 있음

a =  [1,2,3]

print(a[0]) #인덱스 

#리스트의 리스트에 속한 요소 뽑기

a = [1,2,3,['a','b','c']]

print(a[3][0])
#같은 방식으로 삼중 리스트도 가능하다.

#슬라이싱도 가능하다.

a= [1,2,3,4,5]

print(a[0:3])

#리스트 연산 가능  _ 리스트를 합치기 

#리스트 길이 len 그럼 요소 갯수 나옴, 원소갯수?

#리스트 내의 원소 수정과 삭제

#수정시에 원소 인덱스에 값을 새로 정해주면 된다.
#삭제시에는 del을 사용하여 인덱스 정해주면 해당 인덱스 지정 된 요소 삭

del a[0:2]

print(a)

#리스트 추가 append()
#순서 정하기 sort()

#reverse는 그냥 뒤집기

#index(a)는 a값 받아서 index 위치값 아려준다.

#insert(a,b) a_index위치_ 에 b를 삽입



#튜플

#리스트는[] 로 튜플은 ()로 둘러싼다. 튜플은 변화불가
#리스트는 변화 가능, 


#딕셔너리

#배열, 해시, , 
#key를 통해 value (값)를 얻을 수 있는 장점
# value에는 문자, 숫자 리스트  다 넣을 수 있다.

a = {1:'hi'}

a[2] = 'hello'
#키값 = 벨류값

print(a)


del a[1]
# 키값 삭제하면 키값:벨류값 쌍으로 삭제된다.

# 마무리 

print ("""

준비
절박함

나머지 하나는 개소리 '늙고 즐기자' 아니,
즐기기엔 젊은게 낫다.



""")

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

print(a.keys())

for k in a.keys():
    print(k)


#get 은 x라는 키에 대해 value를 준다.

print(a.get("name"))

# &교집합 간단히 이용

# |합집합


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1&s2)

print(s1|s2)

# 차집합은 -
# 

#집합에 자료값 추가는 add

print(s1.add(7))

print(s1)




a = [80,75,55]

sum = 0
for i in a:

    sum = sum +i

    
avg = sum / len(a)

print(avg)


a= 13

if a % 2 == 0 :
    print("짝수")
    
elif a % 2 !=0:
    print("홀수") 
 

a = "881120-1068234"


print(a[0:6])
print(a[7:14])


a = (1,2,3)




a = {'A':90, 'B':80, 'C':70}


print(a['B'])

sum = 0


while i < 1000:

    for i in range(1,1001):

        if i % 3 == 0:
            sum = sum+i

print(sum)

a = '*'

while i <=5:

    for i in range(1,6):

        print(a*i)


for i in range(1,101):
    print(i)


score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for i in score:

    sum = sum+i


print(sum/len(score))




