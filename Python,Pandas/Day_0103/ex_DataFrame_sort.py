# --------------------------------------------------------------
# 정렬 다루기
# -인덱스 기준 정렬
# -데이터 기준 정렬
# --------------------------------------------------------------
import pandas as pd
a=pd.read_csv("C:/Users/hoon3/2022빅콘테스트_데이터분석리그_데이터분석분야_챔피언부문_데이터셋_220908/1.ev_app_resident.csv")
a

# [1] 인덱스 정렬 기준 내림차순으로 =======================
b=a.sort_index(ascending=False)
print(b.index,b,sep='\n',end='\n\n')

# 열기준 내림차순
c=a.sort_index(axis=1,ascending=False)
c
c=a.sort_index(axis=1,ascending=True)
c

# [2] 데이터 즉 값 기준 정렬 내림차순으로 ==================
a.sort_values(by=['dow','time_zone'])