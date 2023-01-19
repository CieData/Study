# ----------------------------------------------------------
# 데이터 프레임
# - 판다스의 구조화 데이터 타입
# - 구성 : 행, 열
# - 요소 : 행인덱스, 열이름
# ----------------------------------------------------------
# 데이터 => list데이터
import pandas as pd
data=[[10,20,30],['f','m','m']]
df1=pd.DataFrame(data)
df1

print(df1.index)
print(df1.columns)
print(df1.dtypes)
print(df1.shape)
print(df1.ndim)
print(df1.values)
print(type(df1.values))

data2={'name':['홍','이','박'],'job':['학생', '학생', '주부']}
df2=pd.DataFrame(data2)
df2
print(f'df2 => \n{df2}')

print(f'df2.index   => {df2.index}')
print(f'df2.columns => {df2.columns}')
print(f'df2.shape   => {df2.shape}')
print(f'df2.ndim    => {df2.ndim}')
print(f'df2.dtypes  => {df2.dtypes}')
print(f'df2.values  => \n{df2.values}\n{type(df2.values)}')
