# -----------------------------------------------------------------
# 강아지                                class dog:
# 이름                                      name='메리'
# 성별                                      gender='여'        속성,필드(attribute,field)
# 몸무게  => 속성, 특징, 외형 ==> 변수        weight=3.4
# 색상                                      color='흰색'
# 앉아                                      def sit(): code
# 기다려 => 동사             ==> 함수        def bark(): code   method
# 꼬리친다                                  def tail(): code
# -----------------------------------------------------------------
# 사용자 정의 클래스
class dog:
    #dog클래스로 생성된 모든 인스턴스가 함께 사용
    #class 변수
    legs=4
    #생성자 method : 힙에 생성ㄴ되는 객체 초기화, 데이터 저장
    #인스턴스 마다 고유의 속성 => 인스턴스 변수
    #콜백 함수 : 시스템에서 호출하는 함수
    def __init__(self,name,gender,weight,color):
        print('Dog __init__(ㅋㅋ)')
        self.name=name
        self.gender=gender
        self.weight=weight
        self.color=color
        # self.legs=4 #모든 dog이 같은 데이터
    
    def bark(self):
        print(f'{self.name}가 짖는다.')
    
    def tail(self):
        print(f'{self.name}가 반갑다고 꼬리친다')

    def eat(self,food):
        print(f'{self.name}가 {food}를 먹는다')




mydog=dog('sy','f', 12,'w')
yourdog=dog('ss','m', 8,'r')
brodog=dog('sa','f', 14,'g')

# 객체(인스턴스) 속성 사용----------------------------
# 읽기 => 변수명.속성명
print(mydog.name)
print('클래스 변수 사용',mydog.legs,dog.legs)
# 값 변경 => 변수명.속성명=새로운값
mydog.weight=20
print(mydog.weight)

# 객체(인스턴스) method 사용---------------------------
# 변수명.method명
mydog.bark()
mydog.tail()
mydog.eat('죽')
