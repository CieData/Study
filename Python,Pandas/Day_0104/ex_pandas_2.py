# -----------------------------------------------------
# 데이터 분석 => 기초통계함수, 고유값, 결측치
# -----------------------------------------------------
import pandas as pd
#데이터 정보 확인 함수 ----------------------------------
def printDataInfo(df):
    df.info
    print(df.head)
    print(df.describe(include='all'))
FILE=r'dataFiles\auto-mpg.csv'
auto_mpg=pd.read_csv(FILE,header=None)
auto_mpg
# (2) 데이터 확인
printDataInfo(auto_mpg)
# (3) 컬럼명 추가
# 'mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name'
g=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
auto_mpg.columns=[g]
auto_mpg
# (4) 실제 데이터와 타입이 맞지 않는 데이터 처리
# horsepower => 데이터 값중에 '?' 있어 바로 실수형으로 변환 불가
# (4-1) 해당 컬럼의 데이터 종류 => 고유값 unique()
auto_mpg['horsepower',]
auto_mpg.horsepower.unique()
type(auto_mpg['horsepower'])
# (4-2) 해당 컬럼의 데이터 종류별 갯수 확인 => value_counts()
auto_mpg.horsepower.value_counts()['?']
print(auto_mpg.horsepower.dtype)
auto_mpg.horsepower.astype({'horsepower':'float64'})