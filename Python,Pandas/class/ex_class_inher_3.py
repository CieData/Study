# -----------------------------------------------
# 선생님을 나타내는 데이터 타입 => 클래스
# - 속성/필드
# 이름
# 나이
# 경력
# 과목
# 담당 반
# 시험 난이도
# 수업 인기
# - 메서드
# 가르치다
# 때린다
# 잡는다
# 
# -----------------------------------------------
class teacher:
    # 클래스 변수
    
    # 생성자
    def __init__(self,name,subject,class_num,howlong,hard,popular):
        self.name=name
        self.subject=subject
        self.class_num=class_num
        self.howlong=howlong
        self.hard=hard
        self.popular=popular
    
    # get/set

    # 커스텀 메서드
    def teach(self,cnum,time):
        print(f'{cnum}반은 {time}시에 수업이 시작한다')
    def strike(self,action,who):
        print(f'{action}하고있는 {who}를 때렸다')
    def catch(self, who):
        print(f'도망가고있는 {who}를 잡았다')



# -----------------------------------------------
# 학생을 나타내는 데이터 타입 => 클래스
# - 속성/필드
# 이름
# 나이
# 학년
# 반
# 번호
# 자리
# 성적
# 
# - 메서드
# 공부하다
# 자다
# 먹다
# 시험치다
# 도망가다
# -----------------------------------------------
class student:
    # 클래스 변수
    
    # 생성자
    def __init__(self,name,old,grade,class_num,snum,seat,score):
        self.name=name
        self.old=old
        self.class_num=class_num
        self.grade=grade
        self.snum=snum
        self.seat=seat
        self.score=score
    
    # get/set

    # 커스텀 메서드
    def study(self,subject,time):
        print(f'{self.name}은 {subject}를 {time}만큼 공부했다')
    def sleep(self,where):
        print(f'{self.name}은 {where}에서 자고있다')
    def run(self, where):
        print(f'{self.name}은 {where}에서 도망간다')
    def exam(self, subject):
        print(f'{self.name}은 {subject}시험을 치고있다')
    
# 공통 클래스
# 바꾸고 싶은건 새로 정의
# 그대로 쓸건 냅두고
# 순서는 앞선 친구로
class A(teacher,student):
    def __init__(self,class_num,subject):
        super().__init__(class_num,subject)


a=A(1,'수학')


#부모클래스(a,b,c,d)
#자식클래스(a,c)


# 상속




class A:
    def __init__(self,x,y=1):
        self.x=x
        self.y=y

class B(A):
    def __init__(self,x,z):
        super().__init__(x)
        self.z=z
    

p=B(1,2)
p.z