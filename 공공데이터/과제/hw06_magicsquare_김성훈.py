def m_s():
    #n값 입력
    while True:
        n=int(input('홀수차 배열의 크기를 입력하세요 : '))
        if n%2==0:
            print('짝수를 입력하였습니다. 다시 입력하세요.')
        else:
            break
    print(f'Magic Square ({n}x{n})')

    #마방진 틀 작성
    ms=[[0]*n for i in range(n)]
    
    #첫 좌표 지정
    row,col=0,n//2
    i=1
    while True:
        #수 집어넣기
        if ms[row][col]==0:
            ms[row][col]=i
            i+=1
            row-=1
            col+=1
        #넣으려는 칸이 이미 채워져있는 경우
        else:
            row+=2
            col-=1

        #넣으려는 좌표가 칸을 넘어간 경우
        if row==-1:
            row=n-1
        elif row>=n:
            row%=n
        if col>=n:
            col=0
        elif col==-1:
            col=n-1

        #모든 칸을 채운 뒤 break
        if i>n**2:
            break
    #마방진 그리기
    for x in ms:
        print(*x)
        print()
m_s()
