# --------------------------------------------------------------------
# 모듈 및 패키지 살펴보기
# 
# [조건] 동일한 목표/목적으로 구성됨
# - 모듈 : 변수, 함수, 클래스를 하나의 파일로 묶은 것
# - 패키지 : 모듈들을 하나로 묶은 것
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# 파이썬 기본 제공 모듈, 표준모듈
import math
print(math.pi)
print(math.factorial(5))

import random
a=[i for i in range(1,46)]
b=[]
for i in range(5):
    random.shuffle(a)
    b.append(a[:6])
c=[]
d=[]
while len(d)!=5:
    a=random.randint(1,45)
    if a not in c:
        c.append(a)
    if len(c)==6:
        d.append(c)
        c=[]
b
d
# 파일 입출력 open() 함수랑 함께 사용 --------------------------------------------------------------
import os.path

FILE_NAME='Day_0102/good.txt'
if os.path.exists(FILE_NAME):
    fp=open(FILE_NAME,mode='r',encoding='utf-8')
    print(fp.read())
    fp.close()
else:
    print('존재하는 파일인지 체크하세요')

# exept ---------------------------------------------------
try:
    pass
# 에러 이름 표시
except Exception as e:
    print(f'{e}')
finally:
    print('항상실행')
