# --------------------------------------------
# 다중 상속 살펴보기
# --------------------------------------------
class A:
    def __init__(self,aa):
        print('A.__init__()')
        self.aa=aa
    def play(self):
        print(f'A.play() - {self.aa}하며 놀고 있다.')

class B:
    def __init__(self,bb):
        print('B.__init__()')
        self.bb=bb
    def play(self):
        print(f'A.play() - {self.bb}신나 신나.')
# 자식 클래스
class C(A,B):
    pass
class D(B,A):
    pass
class E(C):
    pass

c1=C('영화')
c1.play()

d1=D('신나 ')
d1.play()
d2=E('z')
d2.aa