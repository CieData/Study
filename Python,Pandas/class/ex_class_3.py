num1=[1,2,3,4]
num2=[1,1,1,1]
msg='good'
greeting='2023'

#연산 => 덧셈,곱셈
num3=num1+num2
data=msg+greeting

print(num3,data)

#반복 =>
num4=num1*3
data1=msg*3
print(num4,data1)

# ----------------------------------------------------------
# point class
# 변수
#   클래스 변수   => color
#   인스턴스 변수 => x,y
# 메서드
#   시스템 메서드 => 생성자 메서드 __init__():
#   getter/setter 메서드 => 비공개 속성 값 읽기/쓰기 메서드
#   비공개 메서드 => 없음( 형식 : def __method())
#   커스텀 메서드 => def ppoint()
#   
# ----------------------------------------------------------

class point:
    #클래스 변수
    color='black'

    #생성자 메서드
    def __init__(self,x,y):
        self.x=x
        self.y=y

    #시스템 메서드 콜백으로 상황이 맞으면 자동 호출
    #객체+객체 시 자동 호출
    def __add__(self,other):
        return self.x + other.x , self.y+other.y
    #객체-객체 시 자동 호출
    def __sub__(self,other):
        return self.x - other.x , self.y - other.y

    #메서드
    def ppoint(self):
        print(f'({self.x},{self.y})')

#객체 생성 -------------------------------
p1=point(10,10)
p2=point(4,4)

p1.ppoint()
p2.ppoint()

print(f'p1+p2 = {p1+p2}')
