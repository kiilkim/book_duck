# 한줄 주석
#  ctrl / 입니다
"""
여러줄
주석
"""
'''
여러줄 
주석2
'''

#  실행
# alt shift f10 파일 선택하면서 실행
# shift f10 현 파일 실행

print("출력")
print(50+20)

# 변수
a=10
b=20
print(a+b)

#자료형
# 정수형,실수형 , 8진수, 16진수
a=3.4
# 8진수
a=0o11
print(a)
# 16진수
a=0x11
print(a)

# 연산자
#  + - * /  **(제곱)   //(몫,나눈결과 정수)  % 나머지
# 우선순위
# 1.괄호
# 2.**
# 3. -
# 4. * / // %
# 5. + -

a=2**3
print(a) #8
a=5/2
print(a) #2.5
a=5//2
print(a) #2
a=5%2
print(a) #1

# 여러변수 할당
a,b=10,20
print(a)
print(b)

# 복합대입연산자
a+=1 #a=a+1
print(a)

# 변수 형 확인
print(type(a))  # <class 'int'>
a=3.4
print(type(a))  # <class 'float'>

# 형변환
print(int(a))  #3 정수형 형변환

# 문자
a='a'
a='aaa'
a="b"
a="bbb"
a="""aaaa"""
a='''bbbb'''
print(a)
print(type(a)) #<class 'str'>

a=123
# 숫자 문자 형변화
print(type(str(a)))

# 문자열 병합
a="kim"
b="gil dong"
print(a+b)



# 문자열 반복
print(a*5)

# 특수출력문자  \' \" \\ \n
print('python\'s good')
print("python\"s good")

# 문자열 길이
a="hello~~"
print(len(a))


# a=10
# b="문자"
# print(a+b) #같은형이 아니면 에러

a="hello~~, python"
print(a[1])  # 0부터 시작  1 번째
print(a[-1]) # n 뒤에서 첫번째
print(a[0:5]) # hello  0~5앞에 까지 뽑아냄
print(a[:5])  # hello  처음부터 5앞에 까지 뽑아냄
print(a[5:])  # ~~, python

#문자에서 글자 하나 변경 => 에러
# a[0]="e" #에러발생
# print(a)

#문자 숫자 출력 + => ,
print("a",100)
a=10
b="사과"
# 출력   바구니에 사과가 10개 있다
print("바구니에 ",b,"가 ",a,"개 있다")

# 출력 포맷   %d   %s   %f   %c   %o   %x   %%
print("바구니에 %s가 %d개 있다" % (b,a))
print("%10s" % b)  #10중에 오른쪽 출력
print("%-10s" % b)  #10중에 왼쪽 출력
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)
print("%-10.4f" % 3.42134234)

# 함수format()
print("바구니에 {0}가 {1}개 있다".format(b,a))

# 문자열 관련 함수
a="hobby"
print(a.count('b'))  # b 개수
# 문자열 찾기
print(a.find('y'))  #4 0~4번째
print(a.find('a'))  #-1 없으면
#문자열 삽입
a=","
print(a.join('abcd'))
# 대문자 upper()  lower()
# 공백 지우기
a="    hi"
print(a.lstrip())
a="hi   "
print(a.rstrip())
a="   hi    "
print(a.strip())
# 문자열 바꾸기
a="java programming"
print(a.replace("java","python"))

# 문자열 나누기
print(a.split()) #공백 기준 나누기
a="a:b:c:d"
print(a.split(":"))




