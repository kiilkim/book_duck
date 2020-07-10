#0710 1교시

# if문


pocket = ['paper','cellphone']

card = 1

if 'money' in pocket:
    print('택시를 타고 가라')

elif card:
    print('택시를 타고 가라')

else:
    print('걸어가라')



#while

treehit = 0

while treehit < 10:
    treehit +=1
    print("나무를 %d번 찍었습니다." %treehit)

    if treehit == 10 :
        print("나무가 넘어갑니다.")


    #break 구문 수행 도중에 빠져나오기

coffee = 10 
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1

    print("남은 커피의 양은 %d개 입니다." % coffee)

    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


    #continue

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0 : continue
    print(a)


marks = [60, 54, 100, 77]

number = 0
for i in marks :
    number = number + 1
    if i >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


#for 과 함께 하는 range 함수

sum = 0

for i in range(1, 11):
    sum = sum + i


print(sum)


output_a = "{:d}".format(100)



print(output_a)


# :d 는 매개변수로 정수만 올 수 있다.

# 날짜/시간출력

import datetime

now = datetime.datetime.now()



# 이렇게 불러와서 인터넷 화면에 실시간 시간 뿌려줄수 있다. js에도 비슷한 기능 있음.

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second

))


# 홀짝의 구분 2로 나눈 나머지가 0 2로나눈 나머지가 1 이렇게 하면 된다. 
