# Series 데이터 연산 수행
# 브로드캐스트
import pandas as pd

sr1=pd.Series([11,12,13,14,15,16])
sr2=pd.Series([-1,-2,-3,-4,-5,-6])
# 일반 연산
sr1+1
sr1-2
sr1*3
sr1/3
sr1//2

# 비교연산
sr1!=15
sr2<=1
sr3=sr1!=13
sr3
sr3*2

# 다른 시리즈끼리 연산
sr1+sr2
sr1*sr2
sr1/sr2

# 길이가 다른 시리즈끼리 연산
sr4=pd.Series([7,7,7])

sr5=sr1+sr4
sr5
sr1>sr4

# 연산 수행 series 연산 메서드

sr5=sr1.add(sr4,fill_value=0)
sr5

