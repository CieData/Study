# -----------------------------------------------------
# 인덱스 다루기
# -----------------------------------------------------
# 모듈 로딩
import pandas as pd
# DF 생성 ----------------------------------------------
df1=pd.DataFrame({'name':['마징가','제트맨','원더우먼'],
    'kor':[87,91,69],
    'eng':[100,0,50],
    'sci':[1,12,1]})

# DF 데이터 확인하기
df1
df1.index
df1.columns

# [1] 특정 컬럼을 행 인덱스 설정 =================================
df1.set_index('name',inplace=True)
df1.reset_index(inplace=True)

# 모든 행에 대한 값을 출력 => DF.loc[행인덱스]
for i in df1.index:
    print(i,df1.loc[i],sep='\n',end='\n\n')

sr1=df1.loc['마징가']
sr1

# [2] 인덱스 부분 변경 ===========================================
# 전체 변경 => df.index=[새로운 인덱스], df.columns=[새로운 인덱스]
# df.rename() 메서드

# 행 인덱스 '마징가,베트맨,원더우먼' ==> '마징가,홍길동,원더우먼'
df1.rename(index={'제트맨':'홍길동'})

df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
df
# 열 인덱스 변경
df.rename(columns={'B':'BB'},inplace=True)
df

# 행 인덱스 변경 => 10,20,30
df.rename(index={0:10,1:20,2:30},inplace=True)
df
# 행 인덱스 변경 => 10,20,30=>'10','20','30'
df.rename(index=str,inplace=True)
df.index

# [3] 새로운 인덱스 지정 설정 =========================================
# df.reindex([새로운 인덱스])
# 기존 인덱스랑 갯수나 이름이 다를 수 있음
df_re=df.reindex(['20','15','10','25'],method='bfill')
df_re

# NaN을 내가 원하는 값으로 채우기 fill_value=값
df_re1=df.reindex(['20','15','10','25'], fill_value='nothing')
df_re1

# [4] 판다스에서 지정하는 기본 인덱스로 초기화 ==========================
# df.resetindex()
# 기존 인덱스 ==> 컬럼으로 추가
df_re1.reset_index(inplace=True)
df_re1