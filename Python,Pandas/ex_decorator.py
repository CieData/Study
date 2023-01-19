# --------------------------------------------------------------------
# 데코레이터
# - 메서드에 명확한 의미 부여
# - 형식 : @xxxx
# --------------------------------------------------------------------
# 클래스 및 메서드 종류
# - 완성된 클래스 => 클래스
# - 미완성 클래스 => 추상 클래스(abstract class)
#                   미구현(코드 없는 메서드) 메서드를 가지고 있는 클래스
#                   abc모듈 포함해서 사용함
# --------------------------------------------------------------------
# 메서드 종류
# - 객체 생성 해야만 활용 가능 => self
#   => 인스턴스 메서드
# - 객체 생성 없이 사용 가능 => cls
#   => 정적 메서드      ---> 객체 없이 사용 가능
#   => 클래스 메서드    ---> 클래스 정보(cls) 가진 객체 없이 사용 가능
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# 학생 정보 클래스
# - 클래스명 : student
# - 속성
#     - 클래스 속성 : school
#     - 인스턴스 속성 : name, number, grade
# - 메서드
#     - 클래스 메서드 : 학교명 출력 가능
#     - 정  적 메서드 : 학교명 출력 가능
# --------------------------------------------------------------------
class student:
    # 클래스 속성
    school = '경주 고등학교'

    # 인스턴스 즉 객체 생성 및 초기화 메서드
    def __init__(self, name, number, grade):
        self.name=name
        self.number=number
        self.grade=grade

    # 객체 미생성으로 사용 가능한 메서드
    @staticmethod
    def showSchoolName(count):
        print(f'[staticmethod]School : {student.school} - {count}')

    @classmethod
    def printSchool(cls,count):
        print(cls)
        print(f'[classmethod]School : {cls.school} - {count}')

# ----------------------------------------------------------------------
# 대학생 정보를 담고 있는 클래스
# 클래스명 : bigstudent
# 속성 : 학교, 이름
# ----------------------------------------------------------------------
class BigStudent(student):
    # 클래스 변수
    school='한국대'
    # 인스턴스 즉 객체 생성 및 속성 초기화 메서드
    def __init__(self, name, number, grade, major):
        super().__init__(name, number, grade)
        self.major=major

# 클래스 및 객체 사용 하기 ----------------------------------------------
print(student.school)
student.showSchoolName(1)
student.printSchool(BigStudent,1)
student.printSchool(1)

BigStudent.showSchoolName(2)
BigStudent.printSchool(student,2)
BigStudent.printSchool(2)