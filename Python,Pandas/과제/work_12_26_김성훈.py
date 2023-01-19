#1.문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
#출력하는 함수를 구현하세요.
msg=['Good','child', 'Zoo', 'apple', 'Flower', 'zero']
def a(msg):
    msg.sort(reverse=True)
    return msg[0],msg[-1]

#2. 문자열을 입력하면 UTF-8로 인코딩된 값을 아래와 같이 출력된 함수를 구현해 주세요.
data='가나다'
a=''
b=''
for i in data:
    a+=hex(ord(i))
    b+=bin(ord(i))

#3. 숫자와 콤마로만 이루어진 문자열 data가 주어진다. 이때, data에 포함되어있는 자연
#수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
data='123,42,98,18'
def c(data):
    to=0
    maxl=0
    minl=10
    for i in data:
        if i.isdigit():
            to+=int(i)
            maxl=max(maxl,int(i))
            minl=min(minl,int(i))
    return data+'의 합 :'+str(to)+', 가장 큰 수 :'+str(maxl)+', 가장 작은 수 :'+str(minl)

#4. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 
#다른 문자로 출력하는 게임으로 아래 조건을 만족하도록 구현하자.
n=int(input())
def d(n):
    nl=''
    for i in range(1,n+1):
        j=str(i)[-1]
        if j=='2' or j=='4' or j=='8':
            nl+='#'
        else:
            nl+=str(i)
    return nl
d(n)

#5. 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.
n=int(input())
def e(n):
    mon=['December','Januaray','Febrary','March','April','May','June','July','Agust','September','October','November']
    sea=['Winter','Spring','Summer','Fall']
    if n>12:
        print('존재하지 않는 월입니다.')
    else:
        if n==12:
            n=0
    return print(mon[n],sea[n//3])
e(n)

#6. 숫자와 화폐단위를 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
n=1234567
s='$'
def f(n,s):
    n=str(n)[::-1]
    c=0
    for i in n:
        s+=i
        c+=1
        if c==3:
            c=0
            s+=','
    return s[::-1]

#7. 입력받은 정수에 대한 약수를 출력하는 함수를 만들어 주세요.
n=1
def g(n):
    l=[]
    for i in range(1,int((n)**(1/2))+1):
        if n//i*i==n:
            if n//i==i:
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
    l.sort()
    return print(l)
g(9)

#8. 입력 받은 메시지 중에서 중복 없이 숫자만 출력하는 함수를 만들어 주세요.
def printnum(s):
    l=[]
    for i in s:
        if i.isdigit() and int(i) not in l:
            l.append(int(i))
    return l

#9. 생일을 입력 받은 후 한국 나이, 외국 나이를 알려주는 함수를 생성해 주세요. 
def old(s):
    print('당신의 한국 나이는 ',2022-int(s[:4])+1,'세입니다.')
    if int(s[5:7])<12:
        print('당신의 외국 나이는 ',2022-int(s[:4]),'세입니다.')
    else:
        if int(s[-2:])<=5:
            print('당신의 외국 나이는 ',2022-int(s[:4]),'세입니다.')
        else:
            print('당신의 외국 나이는 ',2022-int(s[:4])-1,'세입니다.')


#10. 팩토리얼(Factorial)을 while반복문으로 구현해 주세요. 팩토리얼 수를 입력 받아서 
#팩토리얼 결과를 아래와 같이 출력하세요.
while True:
    try:
        n=int(input())
        s=''
        to=1
        if n==0:
            print('0! => 0')
        else:
            while n!=0:
                s+=str(n)+'*'
                to*=n
                n-=1
            print(s[0]+'! =>'+s[:-1]+'='+str(to))
        
    except:
        break

#11. 입력받은 숫자 범위 안에서 소수(Prime Number)를
#찾아서 반환하는 함수를 생성하세요.
def pnum(n):
    pl=[]
    for i in range(2,n+1):
        count=0
        for j in range(2,int(i**(1/2)+1)):
            if i//j==i/j:
                count+=1
                break
        if i!=1 and count==0:
            pl.append(i)
    return pl

#12. 아래 데이터를 저장합니다. 그리고 과목별 최고점수, 최저점수 출력하세요.
#??
dict={'베트맨':{'국어':90,'수학':89,'윤리':98,'국사':99},
     '마징가':{'국어':82,'수학':71,'윤리':80,'국사':91},
     '슈퍼맨':{'국어':77,'수학':100,'윤리':92,'국사':90},
     '슈렉':{'국어':94,'수학':82,'윤리':93,'국사':71},
     '피오나':{'국어':78,'수학':99,'윤리':91,'국사':83}}
l=['국어','수학','윤리','국사']
for i in l:
    maxi=-1
    mini=101
    for j in dict:
        maxi=max(dict[j][i],maxi)
        mini=min(dict[j][i],mini)
    print(f'{i} 최고점수 : {maxi}, 최저점수 : {mini}')

#13. 구구단 n단부터 m단까지를 반복문 1개로 구현하는 함수를 생성하세요.
n,m=2,4
def googoo(n,m):
    for i in range(n,m+1):
        print(f"--[{i}단]--",end='     ')
    print()
    for i in range(1,10):
        for j in range(n,m+1):
            print(f'{j}*{i}={i*j}',end='\t      ')
        print('')
googoo(n,m)

[[print(f'{dan}*{num}={dan*num:0>2}',end='\n' if dan==9 else ' ') for dan in range(2,10)]for num in range(1,10)]

#14. 입력받은 숫자에서 천자리, 백자리, 십자리, 일자리를 출력하세요.
n=12345
def num(n):
    print('숫자:',n)
    s=str(n)[::-1]
    ss=['일','십','백','천','만','십만']
    for i in range(1,len(s)+1):
        print(ss[len(s)-i]+'의 자리 : ',s[-i])

#15. 정수, 실수, 논리, 문자열 등 데이터 입력 시 모두 덧셈한 결과 출력하는 함수를 
#생성하세요.
def addData(*a):
    if len(a)==0:
        return print('None')
    try:
        return sum(a)
    except:
        b=''
        for i in a:
            b+=i
        return print(b)
addData('A','B')

#16. 아래 출력결과가 나오도록 코드를 작성하세요.
for i in range(8):
    print(' '*(7-i)+'*'*(2*i+1)+' '*(7-i))
for i in range(2):
    print(' '*(5)+'*'*(4)+' '*(5))
print('Merry Christmas')
print(' '*(5)+'2023'+' '*(5))

#17. 문자열 ‘Merry Christmas HaPPy New YEaR’에서 대문자는 소문자로, 소문자는 대문자로 
#변환하여 출력하는 코드를 구현하세요.(List Comprehension)
a='Merry Christmas HaPPy New YEaR'
b=[i.lower() if i.isupper() else i.upper() for i in a]
print(''.join(b))

#18. 6가지 연산 결과를 한꺼번에 반환하는 함수를 생성 후 호출하여 결과를 아래와 같이출력해 주세요.
def cal(n,m):
    print(n+m)
    print(n-m)
    print(n*m)
    if m==0:
        print(0)
        print(0)
        print(0)
    else:
        print(n/m)
        print(n//m)
        print(n%m)

#19. 다양한 사람들로부터 개인정보를 입력받는 함수를 구현하세요.
def Info(a):
    l={}
    for i in a.keys():
        l[i]=a[i]
    return l
Info({'age':12,'id':'mm'})

#20. [나의 계산기] 프로그램을 구현하세요.
while True:
    print('------------------------------------------------------')
    print('<나의계산기>')
    print('------------------------------------------------------')
    print('메뉴 선택(1~6)')
    a=int(input())
    if a==1:
        print('숫자 2개 입력')
        b,c=map(int,input().split())
    elif a==2:
        print('{0}+{1}={2}'.format(b,c,b+c))
    elif a==3:
        print('{0}-{1}={2}'.format(b,c,b-c))
    elif a==4:
        print('{0}*{1}={2}'.format(b,c,b*c))
    elif a==5:
        print('{0}/{1}={2}'.format(b,c,b/c)) 
    elif a==6:
        print('나의계산기 프로그램을 종료합니다.')
        break