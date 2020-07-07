#1일차 1.집합 _ 1)~5)
#2일차 1.집합 _ 6)~7)
#3일차 1.집합 ) 8)~9)

#합집합을 코딩 함수로 만들기

def union(a,b):
    c=[]
    for i in a:
        if i not in b:
            c.append(i)

    c = c + b
    c.sort()

    return c

a = [1,2,3]
b = [3,4,5]

print(union(a,b))


# 교집합

def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    

    return c

print(intersection(a,b))

#차집합

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

print(c)
print(d)


#임의의 갯수 집합으로 교집합 ,합집합 구하기

def sum_all(*args):
    total_num = 0
    for i in args:
        total_num = total_num +i
    
    return total_num

print(sum_all(1,2,3,4,5,6,7,8,9,10))


def union_all(*lists):
    #n개의 입력값으로 부터 합집합은 n-1번의 합집합 시도가 필요

    u = union(lists[0],lists[1])

    for i in lists[2:]: #뭔 뜻이지? 
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
e = [10,4,11,12,5]

print(union_all(a,b,c,d))
print(intersection_all(a,b,c,e))


#class로 임의의 집합 문제 무한 생성기 만들기

a = [1,3,4,5,6]
b = [2,4,6,3,0]

c = union(a,b)
d = intersection(a,b)
e = complement(a,b)

print(c)
print(d)
print(e)

# c,d,e 간 어떤 관계가 있을까??

class Sets():                  # 집합의 연산을 Sets이라는 이름의 class로 정의
     def setdata(self,a,b):     # class의 def는 코딩함수가 아니라 매써드 (method)라고 부르며
                                # method는 입력값으로 항상 self를 맨 앞에 써 줘야함 
         self.a = a             # a를 class의 객체변수로 만든다.
         self.b = b             # b를 class의 객체변수로 만든다.
 
     def union(self):           # 합집합을 구하는 매써드
         result = self.b + []
         for i in self.a:  
             if i not in self.b:    
                 result.append(i) 
         result.sort()
         return result
     
     def intersection(self):    # 교집합을 구하는 매써드
         result = []
         for i in self.a:
             if i  in self.b:
                 result.append(i)
         result.sort()
         return result
 
     def complement(self):      # 차집합을 구하는 매써드
         result = self.a + []
         for i in self.b:    
             if i in self.a:    
                 result.remove(i)   
         result.sort()
         return result
         
c = Sets()                # c를 Sets 이라는 class의 객체로 정의합니다.
c.setdata(a,b)            # c라는 객체가 연산할때 필요한 data인 a,b라는 입력값을 넣어서 setdata란 매써드가 a,b를 개체변수로 만듭니다.
                           # 만들어진 객체변수 a,b는 합집합, 교집합, 차집합 매써드로 계산할때 쓰입니다.
print (c.a, c.b)          # c의 객체변수 c.a, c.b를 출력합니다.
print ('{}와 {}의 합집합은 {}이다.'.format(c.a, c.b, c.union()))         # c라는 객체의 변수 a,b를 가지고 합집합을 구한다.
print ('{}와 {}의 교집합은 {}이다.'.format(c.a, c.b, c.intersection()))  # c라는 객체의 변수 a,b를 가지고 교집합을 구한다.
print ('{}와 {}의 차집합은 {}이다.'.format(c.a, c.b, c.complement()))   # c라는 객체의 변수 a,b를 가지고 a-b의 차집합을 구한다.






