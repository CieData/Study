#--------------------------------
# 기    능 : 숫자 덧셈 후 결과 반환
# 함 수 명 : getTotal
# 매개변수 : 미정 *nums => 0~n개
# 반 환 값 : 덧셈결과 
#--------------------------------
def getTotal(*nums):
    print(type(nums))
    return sum(nums)

#--------------------------------
# 기    능 : 숫자 2개 덧셈 후 결과 반환
# 함 수 명 : twosum
# 매개변수 : a,b
# 반 환 값 : 덧셈 결과 
#--------------------------------
#Default value 기본값 - 함수 호출 시 인자를 주지 않는 경우 사용되는 값, 값 지정시 기본값 무시
def twosum(a,b=0):#b=기본값
    return a+b

#--------------------------------
# 기    능 : 2개 이상의 데이터 덧셈 후 결과 반환
# 함 수 명 : addmore
# 매개변수 : a,b,*nums
# 반 환 값 : 덧셈결과 
#--------------------------------
def addmore(a,b,*nums):
    # c=sum(nums)
    # return a+b+c
    result=a+b
    for i in nums:
        result+=i
    return result

#--------------------------------
# 기    능 : 회원가입 함수 => id, password,  e-mail ,전화번호,[지역,직업,나이,....]
# 함 수 명 : join
# 매개변수 : id, password, e_mail, phone, *data
# 반 환 값 : 가입을 축하드립니다. 
#--------------------------------
def join(id, password, e_mail, phone, **data):
    personInfo={}
    personInfo['id']=id
    personInfo['password']=password
    personInfo['e_mail']=e_mail
    personInfo['phone']=phone
    
    for key,value in data.items():
        personInfo[key]=value
    # for k in data.keys():
    #     personInfo[k]=data[k]
    return personInfo



# 함수 사용 => 함수 호출 : 함수명(인자)
getTotal(True,False)

twosum(b=1,a=10)

addmore()

join('ciea','s11','@nva','010-',job='tea')
print(type(join),type(sum))

mF=join
mF('1','2','3','4')

funs=[sum,max,min,join]
funs[0]([1,2,3])
funs[1]([1,2,3,4])

