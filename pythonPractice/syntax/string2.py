#0528 생코 문자열처리 2번째

#데이터 처리를 잘 할 수록 더 잘다룰 수 있다.

a ='Hello Python' #변수 선언

print(a)


#몇개의 문자인지 알아내는 것 _ 검색을해보자 java에서는 .length로 파악


print(len(a))  

#llo만 추출? slicing: 원하는 것만 추출하기  index 는 0 부터 시작 

print(a[2:5])

#repeat 반복 

print((a+'\n')*3)


#문자열처리 3번째 영상

# 치환
# _ 변수와 포멧팅이 얼마나 중요한가 ?
# _ web application 구현에 중요. 

name = 'apple'

print('to '+name+' hi my name is grape oh,' 
+name+ 'do you wnana to stuydy python?')

#극단적으로 1억번 바꿔야 한다고 생각해보자.. 
print("to '+name+'. Lorem ipsum dolor sit amet, 
consectetur adipisicing elit, sed do eiusmod tempor
 incididunt ut labore et dolore magna aliqua. Ut 
 enim ad minim apple veniam, quis nostrud exercitation 
 ullamco laboris nisi ut aliquip ex ea commodo consequat.
  '+name+' Duis aute irure dolor in '+age+' reprehenderit 
  apple computer in voluptate velit esse cillum dolore eu
   fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui '+name+' officia deserunt
     mollit anim id est laborum.")



