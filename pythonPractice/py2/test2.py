# py2\test2.py
# pandas 설치 : R을 보고 만든 파이썬 패키지
#             : Numpy기반으로 만들어짐 , 복잡한 데이터 분석
# dataframe 기반 => 엑셀 table,  2차원배열(리스트) 행,열

# 파일 웹, sns, csv,xml,xls,json,.... 데이터 수집
# 정제 : 이상한 데이터 1~100 999 -> 처리
#       비어있는 데이터 -> 처리
# 요약 정리 표 -> 시각화(그래프)
# https://pandas.pydata.org/

import pandas as pd

# Series 1차원 테이블
s1=pd.Series([10,20,30,40,50])
print(s1)
# index 번호 values 값
print(s1.index)
print(s1.values)

s2=pd.Series(['a','b','c',1,2,3])
print(s2)

import numpy as np

s3=pd.Series([np.nan,10,30])
print(s3)

index_data=['2020-05-22','2020-05-23','2020-05-24']




# DataFrame 2차원 테이블


