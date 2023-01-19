# ----------------------------------------------------
# 연산자(operator) => 산술,비교,논리,멤버,대입
# 객체의 연산
# - list + list    || list * 정수
# - tuple + tuple  || tuple * 정수
# - str + str      || str * 정수
# ----------------------------------------------------
# ----------------------------------------------------
# 평면에 점을 나타내는 데이터 타입의 클래스
# - 좌표(x, y)  => 속성
# - 메서드      => 점 찍다
# ----------------------------------------------------
class point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def ppoint(self):
        print(f'({self.x},{self.y})')


    def __add__(self,other):
        return self.x + other.x , self.y+other.y
    #객체-객체 시 자동 호출
    def __sub__(self,other):
        return self.x - other.x , self.y - other.y
# ----------------------------------------------------
# 객체 생성
p1=point(1,1)
p2=point(100,100)
p1.ppoint()
p2.ppoint()

result=p1+p2
result