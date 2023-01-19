# -------------------------------
# 스코프(scope) 존재할 수 있는 범위
# -------------------------------
# 변수 종류
# - 전역변수(Global Variable) : 파일 전체에서 사용되는 변수, 같은파일에 존재하는 함수, 클래스 등등 함께사용
# - 지역변수(Local Variable) : 특정 영역 안에서만 사용 가능
#
# 전역변수와 지역변수의 변수명이 동일한 경우
# - 같은 영역안에 있는 변수 우선
# -------------------------------
year = 2022
month = 12
def showToday(day):
    #전역변수 사용 알림
    global year
    year+=1
    print(f'오늘은 {year}년 {month}월 {day}일 입니다.')
print(f'[Before] year=>{year}')
showToday(26)
print(f'[After] year=>{year}')