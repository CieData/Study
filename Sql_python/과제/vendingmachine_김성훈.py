#학번...? ,김성훈
money=10000
coin=100
water=1000
coffee=500
p=500
s=500
cup=300
b=int(input('동전을 투입하세요 : '))
if b>=300:
    while True:
        print('-------------------------------------------------------')
        print('1:블랙커피\n2:프림커피\n3:설탕프림 커피\n4:재고현광\n5:종료\n')
        a=input('메뉴를 선택하세요 : ')
        if a=='5':
            print(f'종료 선택 => 종료합니다')
            break

        elif a=='1' or a=='2' or a=='3':
            if b<300:
                print(f'잔돈 부족 => 잔돈 : {b}\n종료합니다')
                break
            else:
                money+=300
                coin-=3
                cup-=1
                b-=300
                if a=='1':
                    water-=100
                    coffee-=30
                    print(f'블랙커피 선택 => 잔돈 : {b}')
                elif a=='2':
                    water-=100
                    coffee-=15
                    p-=15
                    print(f'프림커피 선택 => 잔돈 : {b}')
                elif a=='3':
                    water-=100
                    coffee-=10
                    p-=10
                    s-=10
                    print(f'설탈프림 커피 선택 => 잔돈 : {b}')
        else:
            print(f'-재고 현황-\n커피 : {coffee}g\n프림 : {p}g\n설탕 : {s}g')
            print(f'물 : {water}ml\n종이컵 : {cup}개\n자판기 잔액 : {money}원\n남은 동전 개수 : {coin}개\n잔돈 : {b}원')
        print('-------------------------------------------------------')
else:
    print(f'돈이 부족합니다 => 투입된 금액 : {b}\n자판기 종료')

            
        