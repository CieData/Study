# ------------------------------------------------
#연락처 프로그램을 구현하고자 한다.
# ------------------------------------------------
# 기능 => 연락처 저장/삭제/수정
# 데이터 => 이름,전화번호,사진,별명,직장,그룹,이메일
# ------------------------------------------------
# (1) 연락처에 사용될 클래스를 생성하세요.
#
# ------------------------------------------------
class contact:
    #클래스 변수

    #생성자
    def __init__(self):
        self.mem=member()

# ---------------------------------------------------------
# 연락처 프로그램 데이터 클래스 => 데이터 타입
# - Member
# - 필수 데이터 => 전화번호, 이름, 이메일
# - 선택 데이터 => 별명, 사진, 주소, 생일
# ---------------------------------------------------------
class member:
    #클래스 변수
    
    #생성자
    def __init__(self,phone,name,email='',alias='',picture='',addr='',birth=''):
        self.phone=phone
        self.name=name
        self.email=email
        self.alias=alias
        self.picture=picture
        self.addr=addr
        self.birth=birth
        
    #getter/setter(비공개 변수)

    #커스텀 메서드
    def info(self):
        print(f'---{self.phone}---')
        print(f'이름   : {self.name}')
        print(f'이메일 : {self.email}')
        print(f'별명   : {self.alias}')
        print(f'사진   : {self.picture}')
        print(f'주소   : {self.addr}')
        print(f'생일   : {self.birth}')

mem=member('010','kim')
mem2=member('011','sll',birth='9-11')
mem.info()
mem2.info()



# ----------------------------------------------------------
# 은행 관리 프로그램을 구현하고자 한다.
# ----------------------------------------------------------
# 기능 => 계좌 개설, 해지, 입금, 출금
# 데이터 => 계좌번호, 비밀번호, 예금주, 개설날짜, 이율, 잔액
# ----------------------------------------------------------
# (1) 은행에 사용될 클래스를 생성하세요.
#
# ----------------------------------------------------------

# ------------------------------------------------------------------------------
# 은행 프로그램 데이터 클래스 => 데이터 타입
# - account
# - 필수 데이터   => 계좌번호, 예금주, 개설날짜, 이율, 잔액, 주민등록번호, 비밀번호
# - 선택 데이터   => 없음
# - 비공개 데이터 => 주민등록번호, 비밀번호
# ------------------------------------------------------------------------------

class account:
    #클래스 변수
    bank_name='농협'

    #생성자
    def __init__(self,number,name,date,rate,balance,hnum,password):
        self.number=number
        self.name=name
        self.date=date
        self.rate=rate
        self.__balance=balance
        self.__hnum=hnum
        self.__password=password
        
    #getter/setter


    #커스텀 메서드
    def info(self):
        print(f'---{self.number}---')
        print(f'이름 : {self.name}')
        print(f'날짜 : {self.date}')
        print(f'이율 : {self.rate}')
        print(f'잔액 : {self.__balance}')
a=account(333,'김','9/11',2.58,'222,222',989,1234)
a.info()
a.name='서'

