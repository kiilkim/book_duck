a=1
b=2
c=a+b
print(c)


b='coding'

b[:]
print(b[:])

print(b[1:3])

print(b[0:6:2])

print(b[::2])

a='halelujah'

print(a.count('l'))

a=3

print('a는 {}이다.'.format(a))

a = [ ]  # 공집합, 빈리스트 
b = [1, 2, 3] #정수형
c = ['Coding', 'is', 'not', 'difficult'] #문자형
d = [1, 2, 'Math', 'Coding'] #정수와 문자
e = [1, 2, ['Math', 'Coding']] #정수와 리스트 안ㅁ ㅜㄴ자.


#len으로 해당변수에 얼마나 많은 원소가 있는지 확인가능

print(len(c))

# index에서 -로 가면 -1이 마지막 글자를 가리킴


#리스트의 연산

a = [3,5]
b = [4,7]

print(a+b)

a[0] = 7

print(a)

del a[0]

print(a)

a=[1,2,3]

a.remove(3)
print(a)




a=[2,6,3,7,8]

a.sort()

print(a)

a.reverse()

print(a)


a=[0,1,2,3,4]

for i in a:
    print(i) 


b= 0

for i in a:
    b = b + i

print('list a의 요소의 합은 {}이다'.format(b))


b=[]

for i in a:
    b.append(i)
    
print(b)