#0623연습

a=1
b='coding'

print(a+a+a)

print(b+b+b)

c=str(a)

print(c)
print(type(c))


a=3

if a > 0:
    print('{}은 0보다 크다'.format(a))

a=[1,2,3,4,5]

if 2 in a:
    print(a)

for i in [1,2,3,4,5]:
    if i>3:
        print(i)


a = 4

if a < 0:
    print('{} is less than zero'.format(a))
else:
    print('{} is not less than zero'.format(a))


a = [1,2,3,1]
b = [4,5,6]

new_a = []

for i in a:
    if i not in new_a:
        new_a.append(i)

print(new_a)

a=[1,2,3]
b=[4,5,6]
c=a+b

print(c)

#문제는 같은게 있을 경우

a=[1,2,3]
b=[3,4,5]

c=a+b
print(c)

new_c =[]

for i in c:
    if i not in new_c:
        new_c.append(i)

print(new_c)

a=[1,2,3]
b=[3,4,5]

c = []

for i in a: #i에 a모두 대응 i=1 ,i=2, i=3
    if i not in b: #만약 1,2,3이 b에 없다면 c에 1,2,3추가
        c.append(i) # 그러나 3은 b에 있으므로 1,2만 추가됨

c = c + b  #c=[1,2] 와 b=[3,4,5] 합침
c.sort() # 오름차순으로 정렬

print(c)


a = ['apple', 'melon', 'orange'] 
b = ['chicken', 'pig', 'cow']

c=a+b
print(c)

b[1]='melon'

c=[]

for i in a:
    if i not in b:
        c.append(i)

c = c + b
c.sort()
print(c)

# 어디에 쓸 수 있을까 
# 점수가 뭐 90점인 누구를 찾아낼때,
# 

#교집합 구현하기 공통인원소 넣기

a=[1,2,3]
b=[3,4,5]

c=[]

for i in a:
    if i in b:
        c.append(i)

print(c)
#정답

#차집합 구현가ㅣ

a=[1,2,3]
b=[3,4,5]

#c=a-b
#print(c)

c = a + []

for i in a:
    if i in b:
        c.remove(i)

print(c)

#왜 c=a 대신에 c=a+[]일까?  c는 a랑 다르다는 것을 보여주기 위함.
#그냥하면 a에서도 3이 제거되기 때문

#여집합
u = [0,1,2,3,4,5,6,7,8,9,0]
a = [1,3,5,7,9]

rest = u + []

for i in a:
    if i in u:
        rest.remove(i)
print(rest)

#생각하기

a = [1,3,4,5,6]
b = [2,4,6,3,0]

for i in a:
    if i in b:
        a.remove(i)
c = a+b  #결과는 [1,3,5,2,4,6,0]
#근데 [1,4,5,2,4,6,3,0]?
#어렵네 ,


print(c)

#코딩함수를 만들면 한줄로 같은 기능 반복

def plus(a,b):
    c = a+b
    return c

d = plus (100,200)
print(d)

a=[1,2,3,4,5]
b=[3,4,5,6,7]
def union(a,b):
    c=[]
    for i in a:
        if i not in b:
            c.append(i)
    
    c = c + b
    c.sort()
    return c
print(c)

a=[0,2,4]
b=[3,0,99]

c=union(a,b)
print(c)


def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    c.sort()
    return c

a = [1,3,4,5,6]
b = [2,4,6,3,0]

print(intersection(a,b))


def complement(a,b):
    c = a + []
    for i in b:
        if i in a:
            c.remove(i)
    c.sort()
    return c

a = [1,3,4,5,6]
b = [2,4,6,3,0]

c = complement(a,b)
d = complement(b,a)

print('a-b={}'.format(c)) # 1,5
print('b-a={}'.format(d)) # 2,0

#임의의 갯수의 집합으로부터 교집합, 합집합 구하는 함수

def sum_all(*args):
    total_num=0
    for i in args:
        total_num = total_num + i
    return total_num

print(sum_all(1,2,3,4,5,6,7,8,9,10))


def union_all(*lists):
    #여러개의 입력값으로부터 합집함 구하기
    #list_a,list_b,list_c 로부터 합집합을 구하려면 2번의 합집합이
    #필요한데, n개의 입력값으로부터 n-1번의 합집합이 필요하다
    u = union(lists[0],lists[1])
    for i in lists[2:]:
        u = union(u,i)
        u.sort()
    return u




def intersection_all(*lists):
    d = intersection(lists[0],lists[1])
    for i in lists[2:]:
        d = intersection(d,i)
        d.sort()
    return d

a = [1,3,6,5,7]
b = [1,5,2,7,3]
c = [4,2,8,9,5]

print(union_all(a,b,c))
print(intersection_all(a,b,c))

