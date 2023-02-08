print('hi')
a <- c(1,2,3)
a
3+5
8-3
3*8
12/4
5**2
5^2
11%%4
18%/%3

2 > 5
2 >= 6
4 == 4
5 != 5
3 | 4
3 & 4

4 > 3 && 3 == 3
4 < 3 & 2 == 2

a<-c(1,2,4)
b<-c(1,2,3)

# 같은 결과
x<-c(1,2,4)
x = c(1,2,4)

sum(x)
mean(x)


a = 1
b = 3
ab = a+b
a = a+1

a.b.c=1
a_b=1
# 객체 이름의 첫글자가 _나 숫자가 올 수 없다.
1ab=1
_ab=1


r = 4
circle = r**2*pi


total = 3500
n = 30
avg = total/n
avg


x = 'char'
# 객체 타입 알려준다
mode(x)

x = 5
is.character(x);is.numeric(x);is.double(x)

real = 3.5
as.integer(real)

intg = 3
is.integer(intg)

intg2 = as.integer(3)
is.integer(intg2)

num = c(1,2,3) # num
ch = c('r','n','y') # char
lo = c(T,F,F,T) # logical
num2 = c(1,2,'r','y') # char
lo2 = c(T,F,1,2) # num
ch2 = c(T,F,'r') # char

x = c(1,2,3,4)
y = c(1,2,3)
x + y
x - y
x * y
x / y


A = T; B = F; C = c(T,T); D = c(F,T)
A & B
A && B
C & D
C && D

A | B
A || B
C | D
C || D


a = c(1,2); b = c(2,2); d = c(3,4)
a < b
a <= b
a < d
a <= d
a > b
a >= b

A = c(T,T); B = c(F,T); C = c(T,T); D = c(T,F)
A == B
C == D
all(A == B)
all(A == C)
any(A == B)
any(A == C)

x = c(-5,10,2,5,8,9); range(x)
var(x)


x = c(55,65,50,60,45)
y = c(1.68,1.70,1.60,1.65,1.62)

bmi = x/(y^2)

mean(x)

s = sqrt(sum((x-mean(x))^2)/(length(x)-1))
s

sd(x)

x = 1:100
x = seq(1,100,2)

x = 1:10
y = 3.3:8
x; y
x = 100:1

rep(c(1,2), times=3)
rep(c(1,2), each=3)


#연습문제
#1.
x = c('0','21','12','16')
#2.
x = as.double(x)
#3.
x = sort(x)
#4.
y = seq(0,30,10)
#5.
x<y & x<=y
#6.
z = rep(c(T,F),times=5)
x <- c(1,10,100)
y <- c('5','5','5')
x<y

vec = vector() #빈 객체
vec = 1:10 # 숫자형
vec2 = c('abc','def') #문자형
vec3 = c(T,F,T,F) #논리형

names(vec2) = c('first','second')

vec4 = vector()
vec4[1] = 1; vec4[2]=5; vec4


# 행렬
x1 = matrix(1:10, nrow=5,ncol=2,byrow=T) #byrow=T 행기준
x2 = matrix(1:10, 5, 2, byrow=F)
cbind(x1, x2) #행을 기준으로 열을 붙임
rbind(x1, x2) #열을 기준으로 행을 붙임


A <- matrix(1:12, 4, 3)
rownames(A) <- c('n1','n2','n3','n4')
colnames(A) <- c('x1','x2','x3')
A
rname <- c('n1','n2','n3','n4')
cname <- c('x1','x2','x3')
B <- matrix(1:12, 4, 3,dimnames=list(rname,cname))
B


#행렬 형태로 들고 오려면 , 필수  여기서 -x값은 제외, 지정값 아님
A[1:2];A[2,3]
A[1,]
A[,2]

A[c(1,3),1]
A[,1:2]
A[,-3]

A <- matrix(1:12,4,3); B <- matrix(1,4,3)
A + B; A - B

A <- matrix(1:6,2,3); B <- matrix(1,3,2)
A %*% B

A <- matrix(1:4,2,2)
# 역행렬
solve(A)

A <- matrix(1:12,4,3)
#전치행렬
t(A)
trace(A)
A <- matrix(1:4,2,2)
det(A)

lst1 = list(a = 1:10, b= matrix(1:4,2,2))
lst1

lst2 = list()
lst2[[1]] <- matrix(1:10,5,2)
lst2[[3]] <- lst1
lst2[[2]][2] <- 12
lst2[[3]]

lst1[[1]]
lst2[[1]]
lst2[[1]][3]
lst2[[3]][[1]]


grade <- c('A','A','B','C','B','B')
f.grade <- factor(grade)
f2.grade <- factor(grade,order=T)
lev <- c('C','B','A')
f3.grade <- factor(grade,levels=lev,order=T)
levels(f2.grade)
levels(f3.grade)


x1 = 1:4
x2 <- c('Kim','Lee','Jung','Park')
dat = data.frame(x1,x2)
dat
dat2 = data.frame(num=x1,name=x2)
dat2
dat2[1:2,]
is.numeric(dat2$num)

str(dat2)
summary(dat2)

x1 <- array(1:24, dim=c(4,3,2))
x2 <- array(1:32, dim=c(2,2,4,2))
x2

x <- 1:25

d <- data.frame(a=1:10, b=rep('A',10), c=rep(T,10))
m1 <- as.matrix(d)
m2 <- as.matrix(d[,1])
d1 <- as.data.frame(m1,stringsAsFactors = F)
d1
d2 <- as.data.frame(m2,stringsAsFactors = F) 
d2

#options 전역매개변수 디폴트값 설정
options(stringsAsFactors=F)



###############################
# 실습 문제
#1. 등차수열 1,3,5,... 를 1부터 30까지 생성하여 x에 저장하시오.
x <- seq(1,30,2)
#2. ‘A’,’B’,’C’의 값을 10번 반복하여 30개의 원소를 갖는 문자열 벡터 y를 생성하시오.
y <- rep(c('A','B','C'),10)
#3. 0,1을 각각 15번 씩 반복하여 길이 30인 벡터 z를 생성하고 이를 문자형으로 변환하여 z1에 저장하시오.
z1 <- as.character(z <- rep(c(0,1),each=15))
#4. 1번의 x를 이용하여 6 x 5 의 행렬을 생성하고 xmat 변수에 저장 하시 오. (행기준으로 채움)
xmat <- matrix(x,6,5)
#5. 1,2,3의 결과를 각각 성분으로 갖는 리스트 생성하시오.
lst <- list(x,y,z)
#6. x,y,z1을 변수로 갖는 데이터프레임을 생성하고 dat로 저장하시오. (문자열 요인화 방지)
dt <- data.frame(x=x,y=y,z=z1,stringsAsFactors = F)
#7. 6의 dat 중에서 첫번째와 두번째 변수를 선택하여 행렬로 변환하시오.
dt_mat1 <- as.matrix(dt[1:2])
#8. 6의 dat 중에서 첫번째와 세번째 변수를 선택하여 행렬로 변환하시오.
dt_mat2 <- as.matrix(dt[-2])
#9. 1의 x 벡터에서 10보다 크고 20보다 작은 원소의 합을 구하시오.
sum(x[x>10 & x<20])
#10. 4의 xmat에서 행의 합, 열의 평균, 열의 분산 값을 각각 계산하시오.
#apply(데이터,방향,적용하고싶은 함수)
apply(xmat,1,sum)
apply(xmat,2,mean)
apply(xmat,2,var)


