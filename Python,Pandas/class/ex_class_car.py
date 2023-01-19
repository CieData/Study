class car:
    window=True
    engine=True

    def __init__(self,number,color,brend,wheel,price,category,fuel):
        self.number=number
        self.color=color
        self.brend=brend
        self.wheel=wheel
        self.price=price
        self.category=category
        self.fuel=fuel
        self.human=[]
        self.human_count=0
    def wheelcount(self):
        print(f'{self.category}이기에 바퀴가 {self.wheel}개이다')
    
    def sell(self):
        if self.color in ['black','white']:
            print(f'색상이 {self.color}이기에 중고차 가격이 높다')
        else:
            print(f'색상이 {self.color}이기에 중고차 가격이 낮다')
    
    def discount(self):
        if self.fuel=='전기':
            print(f'{self.fuel}자동차는 보조금이 나온다')
        else:
            print(f'{self.fuel}자동차는 보조금이 안 나온다')
    
    def boarding(self,*name):
        self.human.append(name)
        self.human_count+=len(name)

    def quit(self,*name):
        if name in self.human:
            self.human.remove(name)
            self.human_count-=len(name)
            print(f'차에서 {name}이 내려서 남은 사람은 {self.human}이고 {self.human_count}명이 남았습니다')
        else:
            print(f'{name}은 차에 타고있지 않습니다.')
    
    def who(self):
        print(f'지금 차에 타고 있는 사람은{self.human}이며, {self.human_count}명입니다.')

    def clear(self):
        self.human=[]
        self.human_count=0
        print('목적지에 도착하여 차에서 모든 사람이 내렸습니다')
    
    #소멸자 method -시스템에서 자동 호출 즉 callback
    def __del__(self):
        pass
    

# mycar=car('257더 555','white','hyundai',4,'2000','SUV','전기')
# mycar.wheelcount()
# mycar.sell()
# mycar.discount()
# mycar.boarding('사람','dd')
# mycar.who()

# yourcar=car('215구 112','black','bmw',4,'5000','SUV','경유')
# yourcar.boarding('람')
# yourcar.who(5)


# ------------------------------------------------------------------------
# 인스턴스와 클래스
# ------------------------------------------------------------------------
# car 인스턴스
mycar=car('222더 555','white','hyundai',4,'2000','SUV','전기')
mycar.__dict__#인스턴스 현재 속성값
mycar.__class__#인스턴스 클래스 정보
car.__dict__
for i in mycar.__dict__.items():
    print(i)