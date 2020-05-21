# test9.py

# 패키지 : 파이썬파일 계층적으로 관리, 폴더
#         폴더.폴더.파일이름

# ptest.py파일 가져오기
import py1.py1_1.py1_2.ptest
py1.py1_1.py1_2.ptest.prn()

import py1.py1_1.py1_2.ptest as pt
pt.prn()

from  py1.py1_1.py1_2.ptest import prn
prn()

