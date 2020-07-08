#회사 대표격의 사람 정보를 알고 있는건 기본. 


#integer 과 floating point 는 알아둬야 한다 정수/실수

#print(temp3_list, temp4_lis


temp_dice : {"age:28","name:kevin"}

# xml 을 이전에 많이 주고 받음. 


#items 
#key value 등 

#enumerate 



dict_a = { 

    "name" : "이경숙",
    "age" : 57,
    "방문횟수" : 15
}


print(dict_a)

#조건문
#선택을 위함이다.





def upCount(a):

    if a >= 10 :

        print("{}는 10 이상입니다.".format(a))
    else:
        print("{}는 10보다 작습니다.".format(a))


print(upCount(15))




# 이름을 넣으면 딕셔너리에서 이름값과 매칭 한 후 
# 몇번 방문했는지, 남아있는 쿠폰횟수가 몇번인지 등 ?


# if를 연속적으로 쓰면 다른거다. elif는 물고 들어가는 것인 반면

x = 10

under_20 = x < 20

print("under_20", under_20)

print("not under_20",not under_20)


number = 273


if number>0 :
    print("양수")

if number == 0 :
    print(0)

if number < 0 :
    print("음수")



#2교시

menu = input("메뉴를 입력 해 주세요.")

print(menu)


if menu == "I" :
    print("정보를조회합니다.")

elif menu == "R" :
    print("정보를조회합니다.")

elif menu == "D":
    print("정보를 삭제합니다.")



#for

for i in range(10):
    print(i)

#range는 범위다 들어간 숫자의 -1 까지 0 부터


for i in range(10):
    print("출력")

    #index가 넘어오는게 아니라, value 값이 넘어온다. 
 
array = [273,23,103,57,52]

for element in array:
    print(element)




# 메뉴마다 새로 하기 귀찮다. 그러면

for val in range(3):
    
    menu = input("메뉴를 입력 해 주세요.")

    
    if menu == "I" :
        print("정보를조회합니다.")

    elif menu == "R" :
        print("정보를조회합니다.")

    elif menu == "D":
        print("정보를 삭제합니다.")

#로직 여러번 물어볼 경우 . 

#원하는데까지 물어보는게 while 이다.



#몇번째인지 알아내는 방법

array = [273, 32, 103, 57, 52]

for i in range(len(array)):

    print("{}번째 반복 : {}".format(i,array[i]))



#int 타입인자 str 타입인지에 따라 수행하는 함수도 있다.



#가끔 건너뛰고 싶을땐 continue ,멈추려면 break 

#위에서 아래로 흘러가도로 로직짜는게 중요''



while True :
    menu = input()
    
    if menu =="I":
        pass
    #틀 잡아놓고 pass 부분만 로직 짜야할 부분 

    if menu == "R":
        pass
    if menu == "Q":
        break

    # 로직다시 짤때 pass 만 검색해서 들어가면 된다. 


#루프안에 루프를 쓰면 머라고 한다. 왜? 

# 불필요하게 돌아가는 로직이 많다..  공회전을 계쏙 하는 것이다.

# 품






#3교시

#고객 정보 관리 시스템 RFP

# 데이터를 어떻게 저장하는가? 변수하나씩 no 
# dictionary ? 노 list 가 가장
# dict 는 개인정보 list는 다수, 그래서 dict를 list안에 

# 그러나 대규모에는 잘 사용안하고 있다. . 
# 리소스기반 클래스기반으로 했는데,, 파이썬이 기능이 너무 좋아서,,안됨
# 그래서 아직 한국에선 자바?
# 그래서 아키텍쳐 할 때 품질 어떻게? 




# 이건 아닌듯, 이건 내가 입력하느것이잖아 상대방이 입력하도록 받아야지





# 마지막 고객에 >= 인 이유는 insert 만 생각하면 이상한데, 다른걸 생각해야함. 








pi = 3.14159265
r = 10

print("원주율 =", pi)











































































































































































