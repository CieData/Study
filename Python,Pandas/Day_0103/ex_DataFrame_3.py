# ----------------------------------------------------------
# 데이터 프레임 행/열 삭제
# ----------------------------------------------------------
# 패키지, 모듈 로딩 -----------------------------------------
import pandas as pd
# DF 객체 생성 ----------------------------------------------
df1=pd.DataFrame({'name':['마징가','제트맨','원더우먼'],
    'kor':[87,91,69],
    'eng':[100,0,50],
    'sci':[1,12,1]})
df1
df1.index
df1.columns

# 행 삭제 => drop() 메서드
# 베트맨이 있는 가로 라인 데이터 삭제
# - inplace True 원본 데이터 적용  None 반환
retDF=df1.drop(1)
retDF,df1

retDF.drop(2,inplace=True)
retDF

# 열 삭제 = > drop(axis=1)
retDF.drop('sci',axis=1)




# ----------------------------------------------------------
# 데이터 프레임 행/열 추가
# ----------------------------------------------------------
# 행 데이터 추가
df1.loc['k']=['너',100,100,100]
df1


# 열 데이터 추가
df1['mat']=[0,0,0,0,0]
df1
df1.loc['a']={'name':'니','eng':0,'kor':1,'sci':2,'mat':3}
a={'name':['마징가','제트맨','원더우먼']}
a['name'].append('f')
a