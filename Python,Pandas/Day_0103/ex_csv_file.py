# -----------------------------------------------------
# csv file ==> dataframe 객체로 지정
# ----------------------------------------------------- 
import pandas as pd
a=pd.read_csv(r'dataFiles\banklist.csv')
a.info()
a.describe(include='all')
a.shape
a.head(10)
a.columns

# (1) 4개 컬럼 사용 'Bank Name', 'City','Closing Date', 'Updated Date'
# (2) 컬럼 중에서 인덱스로 설정
# (3) 'Updated Date' 기준으로 가장 최근 날짜부터 정렬
from datetime import datetime
def ymd(date):
    result = datetime.strptime(date[:-2]+'20'+date[-2:], '%d-%b-%Y').strftime('%Y-%m-%d')
    return result
def ymd1(date):
    result = datetime.strptime(date, '%d-%b-%y').strftime('%Y-%m-%d')
    return result

b=a[['Bank Name', 'City','Closing Date', 'Updated Date']]
b.set_index('Bank Name',inplace=True)
b['Updated Date']=b['Updated Date'].apply(ymd)
b.sort_values(by=['Updated Date'], ascending=False,inplace=True)

b['Updated Date'].values
pd.to_datetime('13-Oct-00')
b