class stack:
    def __init__(self,top=1):
        self.l=[]
        self.top=top

    def size(self):
        return len(self.l)
    
    def allshow(self):
        if self.size()>0:
            print(f'[공의 개수] : {self.size()}')
            print(*self.l[::-1])
        else:
            print('케이스가 비어있습니다.')

    def pop(self):
        if self.size()>0:
            print(f'Pop({self.l[-1]})')
            self.l.remove(self.l[-1])
            self.top-=1
            self.allshow()
        else:
            print('케이스가 비어있습니다.')
        

    def push(self):
        if self.top!=6:
            self.l.append(self.top)
            self.top+=1
            self.allshow()
        else:
            print('케이스가 꽉 찼습니다.')

    def start(self):
        while True:
            print('-'*20)
            print('1. 테니스 공 넣기')
            print('2. 테니스 공 꺼내기')
            print('3. 테니스 공 개수 출력')
            print('4. 종료')
            menu=int(input('메뉴를 선택하세요 : '))
            if menu==1:
                self.push()
            elif menu==2:
                self.pop()
            elif menu==3:
                self.allshow()
            elif menu==4:
                break
            else:
                print('잘못된 메뉴 선택입니다.')
        
a=stack()
a.start()