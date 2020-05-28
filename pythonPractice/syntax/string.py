
#0527 생코_python 
#문자열을 표현하는 방법 1


#print(hello world)는 안됨 ""가 없어서
# "", '' 둘중 하나, 시작과 끝은 같아야 한다.


print("hello world!")

print('hello world')


print("hell'o' world")

#escape
print("hello \'w\'orld")


#newLine

print('hello') #줄바꿈 표현

print('h\nello' ) # 줄바꿈 의미하는 것

#docstring
#그 html의 pro 와 비슷한건데 더욱 자유도가 높다.
#입력하는 그대로 입력 된다. 


print('''

안녕하세요 트럼프는 완전 개 스래기 입니다.

    입방정을 놀렸다고 하면 아주 그냥 

''')
#숫자형 

for a in [1,2,3]:
    print(a)

a=4.24e10

print(a)




def gop(a,b):
    c = a**b
    return c

print(gop(2,3))


a = 14//3

print(a)

b = 14%3

print(b)


#문자형_책

#따옴표로 둘러싸여 있으면 다 문자열이다.

"python"


#"" 안에  '' 가 포함되어야지 역은 인식하지 못한다.



food = 'Python\'s favorite food is perl'

print(food)


multiline = "life is too short \n so, lets do by yourself"

print(multiline
)

#이스케이프 코드

# \n(줄바꿈) \t(탭간격) \\ (백슬래시넣기) \', \"(',"넣기)



#문자열 더하기 

head = "python"
tail = " is tail" #공백도 먹힌다. 

print(head+tail)


for a in ["python is too fast"*2]:

    print(a)


a = 'life is too short to spend in playing games'

len(a)

print(len(a))

print(a[-3])

#문자열 슬라이스

print(a[0:10])

#문자열 포매팅

a = "i eat %d apples" % 3

print(a)

#2개 이상 값 넣기

