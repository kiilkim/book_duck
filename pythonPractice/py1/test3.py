# test3.py
# 제어문 (반복문) while for

# 1~10 출력
i=1
while i<=10:
    print(i)
    i=i+1

# break  반복문 빠져나올때
while True:
    print("무한반복")
    break

# continue 반복문 맨처음 이동
# 1~ 10 반복  출력  3의 배수는 출력하지 않음
i=0
while i<10:
    i=i+1
    #3의 배수이면 continue
    if i%3==0:
        continue
    print(i)

# for 변수 in 리스트(튜플,문자열):
#     반복할 명령1
#     반복할 명령2

li=[85,95,90,80,75]
sum=0
for a in li:
    sum=sum+a

print("항목개수:",len(li))
print("점수합계:",sum)
print("점수평균:",sum/len(li))

s="hello"
for a in s:
    print(a)

lis=['hello']
for a in lis:
    print(a)

li2=[(1,2),(3,4),(5,6)]
for (a,b) in li2:
    print(a+b)

# 1 ~ 10 출력   range(시작번호,끝번호앞, 증가값)
# range(1,11,1)
for i in range(1,11,1):
    print(i)

# 2단 출력
#2*1=2
#2*2=4
#..
#2*9=18

for i in range(1,10,1):
    # print(2,"*",i,"=",2*i)
    print("%d*%d=%d" % (2,i,2*i))

# 2~9 단   for안에 for
for dan in range(2,10,1):
    print(dan,"단");
    for i in range(1,10,1):
        print("%d*%d=%d" % (dan,i,dan*i))

# 한줄 for
# [반복실행문 for 변수 in 리스트]
a=[1,2,3,4]
result=[i*3 for i in a]
print(result)

# [조건에 만족하는 반복실행문 for 변수 in 리스트 if 조건]
# 2의 배수를 구해서 i*3
result=[i*3 for i in a if i%2==0]
print(result)

# [반복실행문 for 변수1 in 리스트1 for 변수2 in 리스트2]
# [반복실행문 for 변수1 in 리스트1  if 조건1 for 변수2 in 리스트2 if 조건2]
# 구구단결과
result=[]
result=[dan*i for dan in range(2,10,1) for i in range(1,10,1)]
print(result)


