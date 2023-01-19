# -----------------------------------------------------
# 객체지향언어 ==> 정보은닉(캡슐화)
# 속성/필드   ==> 비공개
# 메서드      ==> 비공개 private --> 
# -----------------------------------------------------
# -----------------------------------------------------
# BIM지수 => 키 몸무게로 계산
# -----------------------------------------------------
class A:
    # 클래스 변수

    # 생성자
    def __init__(self,weight,height,bmi):
        self.__weight=weight
        self.__height=height
        self.bmi=bmi
    
    def calc(self):
        self.bmi=self.__weight/(self.__height/100)**2
    
    def info(self):
        self.calc()
        print(f'{self.__weight}')
        print(f'{self.__height}')
        print(f'{self.bmi}')
    
    #커스텀 메서드

me=A(90,190,22)
me.info()
me.__dict__
me._A__height=150 #사실 공개였나...?
me.__dict__