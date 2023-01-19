# -----------------------------------------------------------------
# 인덱스와 인덱스 라벨(네임) 살펴보기
# - 인덱스 : 판다스 시스템에 지정하는 RangeIndex 정수형
# - 인덱스 라벨 : 시리즈 객체 생성시 사용자가 지정하는 인덱스
# -----------------------------------------------------------------
# Series 객체 생성
# 데이터 1~50 사이의 3의 배수
# 인덱스 : 문자 'a'~
import pandas as pd
data=list(range(3,51,3))
idx=[chr(i) for i in range(97,97+16)]
idx2=[i for i in range(11,11*16+1,11)]
sr2=pd.Series(data,idx,dtype=float,name='하하')
sr2
#요소1
print(sr2['a'],sr2[0])
#요소 여러개
print(sr2[sr2.index[::2]])
#요소 읽기 
#인덱스가 문자열인 경우 [시작 : 끝 +1] X 
#                      [시작 : 끝] O
#                     ex) ['a':'d']==>'a','b','c','d'
print(sr2['a':'d'],sr2[0:3])





sr3=pd.Series(data,idx2,dtype=float,name='하하')
sr3
type(sr3)
#요소1
print(sr3[0])
#요소 여러개
print(sr3[sr3.index[::2]])
#요소 읽기 
#인덱스가 문자열인 경우 [시작 : 끝 +1] X 
#                      [시작 : 끝] O
#                     ex) ['a':'d']==>'a','b','c','d'
print(sr3[0:3])

print(sr3[11],type(sr3[11:12]))

sr3[0]

d=[1]
sr4=pd.Series(d)
print(type(sr4[[0]]))
print(sr4[0])