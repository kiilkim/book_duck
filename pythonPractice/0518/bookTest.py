#무슨 수업을 세번?만에 180페이지를 나가냐고,,,
# 줄줄줄 그냥 개념 떄려박기 짜증난다
#어떻게 쓰는지도 모르는데 씨~~~~~~~~~~~~~~~~~~~~`
#그렇다고 수업안듣고 생코 수업 듣자니,, 그것도아닌것같고

# 다수의 의견이 기본부터 해야한다였고
# 소수의 의견이 그냥 물음부터 나가야 한다 였나
# 너무 조급한가. ? 그냥 대학교 다시 다닌다고 생각하고 하면
# 안되나?  그땐 그냥 뭐 수업을 교수가 개판으로 하든 잘하든
# 그닥 상관안했잖아?

# class 183p~


#a,b가 객체다. a는 객체다. a는 Cookie의 인스턴스이다. 
# 즉 인스턴스란 말은특정객체(a)가 어떤 클래스(cookie)의 객체인지 관계
#설명하기 위함이다. a는 객체 or a는 cookie의 인스턴스

#사칙연산 클래스 만들기
#클래스 구상이 중요하다.

# 사칙연산을 하려면? 수를 받아야 한다.
# 온도 조절을 하려면? 온도값을 받아서 기준에 따라 온도를 올리거나
#내리거나를 조종해야 한다. 

class FourCal(): #클래스 만듦
    def setdata(self, first, second): #매서드 만들기, //매개변수
        #수행문장
        self.first = first     #매서드의 수행문
        self.second = second
        #self 에는(첫번째 매개변수) setdata를 호출한 a가 자동으로전달
    def add(self): #self에 자동으로 a가 입력 된다. 
        result = self.first + self.second
        return result
    
a = FourCal()

b = FourCal()
# a객체 만들고, 그다음 type(a)로 어떤 타입인지 알아보았다.

#숫자 지정
#a 객체에 사칙연산할 숫자 전달해줘야 한다.

a.setdata(4,2)
b.setdata(3,8)

print(a.add())
