x <- c(1,2,3)
y <- c(1,2)
length(y) <- max(length(x),length(y))
z <- data.frame(x=x,y=y)

################################################################
#정규분포
x_mat <- matrix(rnorm(10000),200,50)
apply(x_mat,2,mean)
apply(x_mat,1,sum)
apply(x_mat,2,var)
apply(x_mat,1,var)

set.seed(123)
rnorm(100)

################################################################
#문자열
myname <- 'kim SH'
paste('My name is', myname, sep=' ')
file_id <- 1533
paste('Dataset_',file_id,'.txt',sep='')

test <- c('abcdefg','AFFY1234568')
nchar(test)

substr(test[2],5,nchar(test[2]))


#현재 작업폴더
getwd()

#작업폴더 위치 설정
options(setwd('C:\\Users\\hoon3\\SH_Git\\Study\\R'))

getwd()


#명령어를 통한 직접적인 입력
dat <- data.frame()
dat = edit(dat)
dat



#scan함수를 이용한 자료 입력
x <- scan(file='input_noh.txt', what=numeric())
x
x <- scan(file='input_noh.txt', what=character())
x

dat = read.table(file='input_noh.txt',header = T)
dat






###########################################
#if 문
x <- 1:5
y <- -2:2
if(any(x>0)){print(x)}
if(any(y<0)){print(abs(y))}
if(any(y<0)){
  print(abs(y))
  cat("\n y contains negative values")}

a <- 1
b <- 6
c <- 3
D <- b^2-4*a*c

if(D < 0){
  cat("\n No roots")
  } else  {
  print((-b + sqrt(D))/(2*a))
  print((-b - sqrt(D))/(2*a))
}
ifelse(D < 0, cat("\n No roots"), c((-b + sqrt(D))/(2*a),(-b - sqrt(D))/(2*a)))


tmp <- c(3,-1,1,-2,0)
sn <- ifelse(tmp>0,'pos',ifelse(tmp<0,'neg','zero'))
data.frame(tmp,sn)





##############################################################
#switch 문 여러값에 대해 각각 다른 처리하고자할때
x <- c(1,3,2,5,2)
i <- 5
switch (i, mean(x), median(x), sd(x), var(x))

type <- 'mean'
switch (type, mean=mean(x), sd=sd(x), var=var(x))




########################
#실습문제
x <- c(1,3,2,5,2)
sx <- sum(x)
ifelse(sx>5,'sum(x) is greater than 5',ifelse(sx<5,'sum(x) is less than 5','sum(x) is equal to 5'))
