# ------------------------------------------------------------
# 상속(Inheritance) - 재사용 및 기능 확장
# ------------------------------------------------------------

# ------------------------------------------------------------
# 포인트를 나타내는 데이터 타입 => 클래스
# - 클래스명
#   Point2D
# - 속성/필드
#   좌표 (10,5)
# - 기능/역할
#   점 찍기
#   동그라미 그리기
#   별 그리기
# ------------------------------------------------------------
class P2D:
    # 클래스 변수

    # 생성자
    def __init__(self,x,y=1):
        self.x=x
        self.y=y
    
    # getter/setter

    # 커스텀 메서드
    def ppoint(self):
        print(f'({self.x},{self.y})에 점 찍기')

    def drawCircle(self, action, color='black'):###????? color,action 순서
        print(f'({self.x},{self.y})에 {color}색 {action}동그라미 그리기')
    
# -------------------------------------------------------

class P3D:
    # 클래스 변수

    # 생성자
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    # getter/setter

    # 커스텀 메서드
    def ppoint(self):
        print(f'({self.x},{self.y},{self.z})에 점 찍기')

    def drawCircle(self, action, color='black'):###????? color,action 순서
        print(f'({self.x},{self.y},{self.z})에 {color}색 {action}동그라미 그리기')
    
# 객체 생성
p1=P2D(4,10)
p1.drawCircle(action='사라지는')
p2=P3D(4,10,0)
p2.drawCircle(action='사라지는')

# 상속
class point3d(P2D):
    pass
p3=point3d(3,5)
p3.ppoint()


class point3d(P2D):
    def __init__(self,x,z,y=1):
        #super() 상속 관계에 사용되는 녀석
        super().__init__(x,y)
        self.z=z
    # 부모 클래스로부터 상속받은 메서드의 구현 부분을 변경 => 오버라이딩
    # 메서드명, 매개변수 => 동일
    # 기능 구현 코드 => 변경
    def drawCircle(self, action, color='black'):
        print(f'({self.x},{self.y},{self.z})에 {color}색 {action}동그라미 그리기')
    
p3=point3d(3,z=5)
p3.drawCircle('rr')

class point4d(P3D,P2D):
    pass
p4=point4d(5,2,3)
point4d.mro()