# -------------------------------------------------------
# 연산 실습
# -------------------------------------------------------
import pandas as pd
FILE=r'dataFiles\stock price.xlsx'
a=pd.read_excel(FILE,engine='openpyxl',index_col=0)
def comma(n):
    return format(n,',')
# [1] 주식 ID, 이름, 가격만 사용
a.drop('value',axis=1,inplace=True)
# [2] 가격에 대한 *100 결과를 추가
a['price_100']=a['price']*100
a['price_100']=a['price_100'].apply(comma)
a

# ============================================================
# id 컬럼을 인덱스로 설정하세요.
# index_col=('id'or컬럼명 순서'id'는 0) # 파일 읽을때 pd.read 의 매개변수
# 로딩할 특정 컬럼 지정 => usecols='A,B,D'
a=pd.read_excel(FILE,engine='openpyxl',index_col='id',usecols='A,B,D')
a
# skiprow는 행 지울 개수, header=None으로 지정 해줘야 데이터가 컬럼명이 안됨
# []안에 수 넣으면 지정 행 삭제
a=pd.read_excel(FILE,engine='openpyxl',skiprows=[i for i in range(1,5)])
a=pd.read_excel(FILE,engine='openpyxl',skiprows=lambda x: x in [0,2])
a=pd.read_excel(FILE,engine='openpyxl',skiprows=3,header=0)
a


# parse_dates => 컬럼지정하면 해당 컬럼의 타입이 datetime64로 변경
# dayfirst => 일 - 월 순서로 설정
# infer_datetime_format => 날짜시간 파맷을 추정해서 파싱
# date_parser => 직접 날짜시간 포맷 설정 function
from datetime import datetime
_date_parser=lambda x : datetime.strptime(x,'%d-%b-%y')
b=pd.read_csv(r'dataFiles\banklist.csv',parse_dates=['Updated Date'],dayfirst=True,infer_datetime_format=True)
b=pd.read_csv(r'dataFiles\banklist.csv',parse_dates=['Updated Date'],date_parser=_date_parser)
b.info()
b