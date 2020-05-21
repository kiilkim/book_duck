# test7내용(선생님)

# p171
# 파일 읽고 쓰기
#  파일 사용하기 위한 객체생성
# 변수=open("파일이름","모드")
# 모드 w 파일 내용쓸때  r 파일 읽을때  a 새로운 내용 추가
# f=open("파일.txt",'w')
# f.close()

f = open("새파일3.txt" ,'w')

#앞의""에 경로를 넣어줘도된다. 


for i in range(1, 11, 1):

    data = "%d 번째\n" % i

    f.write(data)

f.close()


# 이렇게 데이터를 인터넷에서 뽑아와서 (경제기사를)
# 어떠한 작업으로 인해 그 30개 중의 기사에서 가장 많이 쓴
# 단어가 무엇인지 그럼 그 관련해서 글을 쓰는것이지.

# 그렇게 글을 쓰다가 (티스토리 ,블로그 )
# 그런 글을 나만의 web이나 앱에 쓰고 어쩌다 유입된 사람들의
# 팬덤을 만드는 것. 그리고 그것을 시작으로 나의 개인 사업랜드
# 구성. 


# filetest.txt 내용 읽어오기
f=open("새파일3.txt","r")


line=f.readline() # 한줄만 읽는다. 


print(line)

while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()


