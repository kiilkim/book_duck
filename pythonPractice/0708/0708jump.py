#02장 자료형

name = "김기일"
age = 30

print(f'나의 이름은 {name} 입니다. 나이는{age}입니다.')


print("어항 온도는 %d도 입니다." % 28)


#여기서 어항 온도의 변화를 보여주려면 28에 해당하는것을
#반복적으로 해주면된다. Iot 기기에서 받은 온도변화를
#DB에 저장하고 그 dB값을 일정시간마다 끌어와서 반영

print("어항 온도는 %s도 입니다." % "이십팔")

#문자열을 넣기 위해서는 %s 써야 한다.


#변수로 대입 가능

for i in range(2):
    number = i

    print("어항의 온도가 %d도 입니다." % number)


number = 28

item = "어항"

print("%s의 온도가 %d도 입니다." % (item, number))


# %s는 포맷코드인데 어떤형태의 값이든 넣을 수 있다.

print("%s의 질산염 농도가 %d%% 입니다." %(item, number))

#% 나타낼떈 %%로!

#정렬과 공백 

print("%10s" % "hi") #오른쪽으로 몰아넣고 총10칸

#왼쪽 이후 공백은 -10으로 하면됨.

print("%0.4f" % 3.42134234) #소수점이하 4개


#format 이용한 포매팅

a = 2 #설정온도 

for i in range(a):

    print("어항의 온도는 {}도로 설정했습니다.".format(i))


print("{0:<10}띄우기".format("hi"))

print("오른쪽으로{0:>10}".format("hi"))


print("{0:=^20}".format("공지"))


d = {'name':'이경숙', 'year':15}

print(f'고객 {d["name"]}은 이용 년수가 {d["year"]}입니다.')


#문자열관련 함수 _ 내장함수 ,, 변수이름뒤 . 붙이면 된다.


a = "hobby"

print(a.count('b')) #a의 변수에있는 글자 'a'의 갯수


#위치 알려주기

a ="파이썬은 최고의 선택이다."

print(a.find("최"))

#위치(인덱스 알려주기
# 
# 

print(a.index("최"))

#문자열 삽입 

print(",".join("1234"))