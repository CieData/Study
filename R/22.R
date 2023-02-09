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

dat = read.table(file='input_noh.txt')
dat
