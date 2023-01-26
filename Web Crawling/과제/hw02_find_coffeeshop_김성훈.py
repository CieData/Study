import pandas as pd
holly=pd.read_csv('hollys_branches.csv')


#1번
def info(df):
    for i in range(len(df)):
        j=df.iloc[i]
        print(f'[{i+1}] : 매장이름 : {j[0]}, 지역 : {j[1]}, 주소 : {j[2]}, 전화번호 : {j[3]}')
    print(f'전체 매장 수 : {len(df)}')
info(holly)

#2번
def location(df):
    while True:
        loc=input('검색할 매장의 도시를 입력하세요 : ')
        if loc=='quit':
            break
        df1=df[df['위치(시,구)'].str.contains(loc)]
        print('-'*20)
        print(f'검색된 매장 수 : {len(df1)}')
        print('-'*20)
        for i in range(len(df1)):
            j=df1.iloc[i]
            print(f'[{i+1}] : [{j[2]}, {j[3]}]')
location(holly)

