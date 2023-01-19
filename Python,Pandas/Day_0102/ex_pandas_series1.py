import pandas as pd
# 시리즈 ================================================
# pandas.Series(데이터)
# 속성 : index, values, ndim, shape,
# ======================================================
# printSeries
def printSeires(srObj,srObjName):
    print(f'{srObjName}===>\n{srObj}')
    print(srObj.index)
    print(srObj.values)
    print(srObj.ndim)
    print(srObj.shape)

# __name__ : 매직 변수, 시스템에 값을 설정
# 해당 파이썬 파일이 실행 중 여부 확인
# 실행 중 ==> __main__
# import 될 경우 ==> 파일명
print(f'{__name__}')

if __name__=='__main__':
    # (1) 데이터 => 리스트 데이터
    sr = pd.Series([10,20,30])
    printSeires(sr,'sr')
    # (2) 데이터 => 딕셔너리 데이터
    sr2=pd.Series({'name' : 'h', 'age' : 12,'loc':'daegu'})
    printSeires(sr2,'sr2')
    # (3) 데이터 => 튜플
    sr3=pd.Series((11,12))
    printSeires(sr3,'sr3')