# -------------------------------------------------------
# 사람 데이터 타입 - 동사무소에서 우리 동네 주민 관리 프로그램
# 속성/성질/외모...
# => 이름, 나이, 주소, 주민번호, 휴대폰, 이메일, 혈액형, 키, 몸무게, 성별, 생년월일, 직업...
# 기능/역할/행동...
# => 자다, 걷는다, 먹는다, 논다, 공부한다, 생각하다, 쇼핑하다..., , , , , , , , , , , 
# -------------------------------------------------------
class jumin:
    #클래스 변수
    __dong='황성동' #비공개, 클래스내에서 사용가능

    #생성자 메서드
    def __init__(self,name,birth,gender,address,age,phone,num,life):
        self.name=name
        self.__birth=birth
        self.gender=gender
        self.__address=address
        self.__age=age
        self.__phone=phone
        self.__num=num
        self.life=life
    
    #getter/setter 메서드
    #전화번호,주소는 변경 가능
    def set_phone(self, phone):
        self.__phone=phone
    def set_address(self, address):
        self.__address=address

    
    
    #커스텀 메서드
    def info(self):
        print(f'{self.name} \n {self.__birth} \n {self.gender} \n {self.__address} \n {self.__age} \n {self.__phone} \n {self.__num} \n{self.life}')




a=jumin('김',9,'m','용',25,8781,989,'청')
a.info()

