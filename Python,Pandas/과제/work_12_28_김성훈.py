# -------------------------------------------------------------------
# 1.계산기 프로그램을 클래스 기반으로 만들어주세요
# -------------------------------------------------------------------
class calc:
    def __init__(self,num=0):
        self.num=num
    def add(self,*x):
        self.num+=sum(x)
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def sub(self,*x):
        for i in x:
            self.num-=i
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def mul(self,*x):
        for i in x:
            self.num*=i
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def truediv(self,*x):
        for i in x:
            self.num/=i
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def div(self,*x):
        for i in x:
            self.num//=i
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def mod(self,*x):
        for i in x:
            self.num%=i
        if self.num==int(self.num):
            return int(self.num)
        else:
            return self.num
    def reset(self):
        self.num=0
        return self.num
a=calc()
a.sub(5.555,5,3)
a.add(5,3,4)
a.mul(3,2)
a.truediv(3,1)
a.div(3,1,2)
# ----------------------------------------------------------------------------------------------------------------------
# 2.함수 구현
#     2-1) 구구단 2~9단 출력 반복문 1개
#     2-2) 리스트 컴프리헨션
#     2-3) 별자리, 띠
# ----------------------------------------------------------------------------------------------------------------------
#2-1) ------------------------------------------------------------------------------------------------------------------
def googoo():
    a=2
    b=1
    for i in range(9):
        if i==0:
            exec("print(f'----{a}단----   ',end='\\n' if a==9 else '\t');a+=1;"*8)
        exec("print(f'{a} * {b} = {a*b}',end='\\n' if a==9 else '\t');a+=1;"*8)
        b+=1
googoo()

def 구구단(n,m):
    a=n; b=1; switch=True
    while b != 10:
        if switch:
            print(f'--[{a}단]--',end='\t')
            a=a+1
            if a==m+1: switch=False; a=n; print()
        if not switch:
            print(f"{a}*{b}= {a*b}",end='\t\t')
            a=a+1
            if a==m+1: a=n; b=b+1; print()

구구단(2,4)
#2-2) ------------------------------------------------------------------------------------------------------------------
a=[[print(f'{i}*{j}={i*j}',end='\n' if i==9 else '\t') for i in range(2,10)]for j in range(1,10)]
#2-3) ------------------------------------------------------------------------------------------------------------------
def human(s):
    a=['원숭이','닭','개','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
    if int(s[:2])>22:
        c=int(s[:2])
    else:
        c=100+int(s[:2])
    star=['',19,18,20,19,20,21,22,22,23,22,22,24]
    star_name=['염소자리','물병자리','물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','궁수자리','염소자리']
    month=int(s[2:4])
    day=int(s[4:6])
    if star[month]<day:
        b=star_name[month]
    else:
        b=star_name[month-1]

    return print(f'{a[c%12+4]} {b}')
human('230101')

