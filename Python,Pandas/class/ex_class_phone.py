# -------------------------------------------------
# 휴대폰
# -------------------------------------------------
# (1) 어떤 클래스          ==> 클래스 클래스명
# (2) 특징/성격/외형/속성들 ==> 변수 속성, 필드
# (3) 기능/역할/행동       ==> 클래스 전용 함수 메서드
# -------------------------------------------------
# 휴대폰 클래스
# -------------------------------------------------
class phone:
    #클래스 변수

    #생성자
    def __init__(self,maker,number,color):
        self.maker=maker
        self.number=number
        self.color=color

    #커스텀 메서드
    def calling(self,phonenumber):
        print(f'{phonenumber}에 전화합니다.')
    
    def mms(self,message):
        print(f'{self.number}가 /{message}/ 를 보냅니다.')
    
    

myphone=phone('삼성','010-1111-1111','purple')
myphone.calling('010-2222-2222')
myphone.mms('집가고 싶다 하하하하하ㅏ')
