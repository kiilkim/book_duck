# test7.py

# p171
# 파일 읽고 쓰기
#  파일 사용하기 위한 객체생성
# 변수=open("파일이름","모드")
# 모드 w 파일 내용쓸때  r 파일 읽을때  a 새로운 내용 추가
# f=open("파일.txt",'w')
# f.write() 함수호출 f.read()  f.readline() f.readlines()
# f.close()
f=open("filetest.txt",'w')
for i in range(1,11,1):
    data="%d 번째\n" % i
    # print(data)
    f.write(data)
f.close()

#  E:/Shared/JSP/workspace_py/py1/filetest2.txt
#  11 ~ 20 파일에 출력
f2=open("E:/Shared/JSP/workspace_py/py1/filetest2.txt",'w')
for i in range(11,21,1):
    data="%d 번째\n" % i
    # print(data)
    f2.write(data)
f2.close()

#  E:/Shared/JSP/workspace_py/py1/filetest.txt
#  11 ~ 20 파일에 추가 출력
# f3=open("E:/Shared/JSP/workspace_py/py1/filetest.txt",'a')
# for i in range(11,21,1):
#     data="%d 번째\n" % i
#     print(data)
#     f3.write(data)
# f3.close()

# filetest.txt 내용 읽어오기
f4=open("filetest.txt","r")
# line=f4.readline()
# print(line)
while True:
    line=f4.readline()
    if not line:
        break
    # print(line)
f4.close()

f5=open("filetest2.txt","r")
lines=f5.readlines()
# print(lines)
for li in lines:
    print(li)
f5.close()

# 파일전체 내용 가져오기 read()
f6=open("filetest.txt","r")
data=f6.read()
print(data)
f6.close()