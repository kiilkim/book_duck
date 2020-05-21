#반복문 .\

#대량데이터를 많이 처리해야 하므로 for,while 등 사용
#반복되는 부분이 탭만큼 띄워짐

i=1
while i <= 10 :
    print(i)

    i+=1


#break  반복문 빠져나오기
#continue: 계속

#while 문 안에서도 if 문 쓰고 텝해서 써야 한다. 



i = 0 

while i<=10:
    i+=1

    if(i%3==0) :
        continue #반복문 맨처음
   

  
    print(i)




#130p예시 나무 꾼

treeHit = 0
while treeHit < 10:
    treeHit +=1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")



#어디서 쓸 수 있나
#어항의 온도, 



#for 변수 in 리스트 (튜플,문자열):
#튜플은 수정 불가, 문자열 : 문자를 여러개 모아서 배열에 담았다. 

#     반복할 명령1
#     반복할 명령2



li = [85,95,90,80,75]

sum = 0 #합계저장

print(len(li))


for i in li:

    sum +=i

print("항목개수:",len(li))
print("점수합계:",sum)
print("점수평균:",sum/len(li))



#138p

test_list=['one', 'two', 'tree']

for i in test_list : #one,two,three순서대로 i에 대입

    print(i)

a = [(1,2), (3,4), (5,6)]

for (first,last) in a:
    print(first,last)
    print(first+last)


#주사위의 합


s="hello"

for a in s:
    print(a)


lis=['hello']

for a in lis:
    print(a)

    #리스트안의 문자열은 하나로 친다. 

#1~10출력  range(시작번호, 끝번호,증가값 )

add = 0
for i in range(1,11,1):
    print(i)
    add+=i

print("총합:",add)




#for응용 139p

scores = [90, 50, 60, 80, 75]

#합격인지 불합격인지 

number = 0 # 학생에게 붙여줄 번호

for score in scores :
    number +=1

    if(score>=60):
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)


#물고기어항 5개

fish_tanksC = [25,27,29,22,26]

number =0


for fish_tankC in fish_tanksC:
    number+=1

    if(fish_tankC >28) :
        print("%d번 어항이 %d도 입니다." % (number,fish_tankC))
    
    elif(fish_tankC <26):
        print("%d번 어항이 %d도 입니다." % (number,fish_tankC))

    else:
        print("%d번 어항은 정상온도입니다." % number)


## 2단 출력
#2*1=2
#2*2=4
#..
#2*9=18

for i in range(1,10,1):

    #print(2,"*",i,"=",2*i)
    print("%d*%d=%d" % (2,i,2*i))

 

# 구구단


for dan in range(2,10,1):

    print("<%d단>" % dan)

    for i in range(1,10,1):
        print("%d*%d=%d" % (dan,i,dan*i))

#한줄 for 문
# 
#[반복실행문 for 변수 in 리스트 ]
# 

a = [1,2,3,4]

result= [i*3 for i in a]

print(result)




#for문과 같이 사용되는 rnage

a = range(10) # 0부터 10 '미만' !


sum = 0

for i in range(1,101):
    sum+=i

print(sum)



scores = []



a = "life is too short, you need python"

if "wife" in a:
    print("wife")

elif "python" in a and "you" not in a:
    print("python")

elif "shirt" not in a:
    print("shirt")

elif "need" in a:
    print("need")

else:
    print("none")

# [조건에 만족하는 반복실행문 for 변수 in 리스트 if 조건]
# 2의 배수를 구해서 i*3


result = [i*3 for i in range(0,101) if(i%2==0)]

#for 문 돌리면서도 2의 배수 찾을 수 있음


print(result)


# [반복실행문 for 변수1 in 리스트1 for 변수2 in 리스트2]
# [반복실행문 for 변수1 in 리스트1  if 조건1 for 변수2 in 리스트2 if 조건2]
# 구구단결과


result = [dan*i for dan in range(2,10,1) for i in range(1,10,1)]

print(result)