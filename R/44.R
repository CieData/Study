iris

str(iris)

colnames(iris)

lm(Sepal.Length ~ Petal.Width, data = iris)
z <- lm(iris[,1] ~ iris[,4])

summary(z)

plot(iris[,1] ~ iris[,4])
abline(z)


zz <-  lm(iris[,1] ~ iris[,2] + iris[,3] + iris[,4])
zz

summary(zz)









install.packages('ROCR') # roc커브를 그리기 위한 패키지
install.packages('e1071')#범주형 로지스틱회귀
install.packages('MASS') #범주형 로지스틱회귀
install.packages('pscl') #
install.packages('caret')#데이터전처리용
install.packages('kernlab')
install.packages('nnet')#인공신경망
install.packages('car') #데이터 전처리
install.packages('SparseM')
install.packages('glmnet') # lasso 변수선택방법
install.packages('elasticnet')
install.packages("corrplot") #다중공선성을 알아보기 위해 상관플롯을 그르기위한 패키지



library("corrplot")
library('elasticnet')
library('glmnet')
library('SparseM')
library('car')#
library('pscl')#
library('e1071')# 범주형 로지스틱회귀
library('MASS')# 범주형 로지스틱회귀
library('caret')#
library('kernlab')
library('nnet')# 인공신경망
library('ROCR')#



data <- read.csv('company.csv', header = TRUE, fileEncoding = 'cp949')
data

str(data)
head(data)
dim(data)

colSums(is.na(data))
for(i in 1:dim(data)[2]){
  data[is.na(data[,i]),i] = median(data[,i], na.rm = TRUE)
}

colnames(data)[20] = '신용평점'
colnames(data)
data$신용평점 <- ifelse(data$신용평점<=5,0,1)
data$신용평점<-as.factor(data$신용평점)
data$신용평점

set.seed(123)
intrain<-createDataPartition(y=data$신용평점,p=0.7,list=FALSE)
intrain
training<-data[intrain,]## 트레이닝데이터
training
testing<-data[-intrain,]## 테스트 데이터 나눔
testing

colnames(data)
m2<-train(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 +
            단기차입금.총자본, data=training, method='glm')
summary(m2)


predictions2<-predict(m2,newdata=testing)
predictions2

confusionMatrix(predictions2,testing$신용평점)




#install.packages('rpart')
library('rpart')
head(training)
m<-rpart(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율
         + 단기차입금.총자본,data=training)
plot(m,compress=TRUE,margin=0.1)
text(m,cex=0.8)
#뭔가 보기 불편함



install.packages('rpart.plot')
library('rpart.plot')
prp(m, type=4, digits=3) # type extra digits 숫자 바꿔보면 더 예쁘게 꾸며짐.
#예측
pre_rpart<-predict(m,newdata=testing)
head(pre_rpart)
head(testing)
pre_rpart<-round(pre_rpart[,2]) # p값을 0.5로 두자.
pre_rpart<-as.vector(pre_rpart)
pre_rpart<-as.factor(pre_rpart)
test_rpart<-testing$신용평점
test_rpart<-as.factor(test_rpart)
confusionMatrix(pre_rpart,test_rpart)



install.packages('randomForest')
library('randomForest')
head(training)
m2<-randomForest(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 +
                   단기차입금.총자본,data=training)
m2
#변수중요도
importance(m2)
#그래프 그리기
varImpPlot(m2)





##인공신경망
m<-nnet(신용평점 ~ 유동비율 + 부채비율 + 순이익증가율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,
        size=5, #은닉층 노드 갯수
        linout=FALSE, # TRUE이면 활성함수가 선형출력(liner output) FALSE면 로지스틱함수가 적용
        MaxNWts=1000, # 가중치의 최대개수로 기본값은 1000, 모델이 복잡하다면 가중치의 수를 증가시켜야함.
        data=training)
#나머지 옵션도 있음. 찾아볼 것.
pre_nnet<-predict(m,newdata=testing)
head(pre_nnet)
pre_nnet<-as.factor(round(pre_nnet))
pre_nnet
#예측
confusionMatrix(pre_nnet,testing$신용평점)


var1<-c(1,2,3,4,5)
plot(var1)

var2<-c(3,3,3)
plot(var2)

x<-1:5
y<-5:1
plot(x,y)

x<-1:3
y<-3:1
plot(x, y, xlab="x축 값", ylab="y축 값", main="Plot Test") 


x1 <- 1:5
y1 <- x1^2
z1 <-5:1
(mat1<-cbind(x1,y1,z1)) # 행렬 생성



par(mfrow=c(2,3)) # 2행 3열
plot(y1, main="index")
plot(x=x1, y=y1, main="x^2")
plot(mat1, main="matrix")
plot(x1, y1, type="l", main="line")
plot(x1, y1, type="h", main="high density")
plot(x1, y1, type="s", main="steps")
par(mfrow=c(1,1)) 





KIS <- read.csv('KIS.csv')
plot(KIS$Trust, KIS$DeR, type="l", main="KIS Chart", xlab="신뢰도", ylab="부채비율")


x=rep(1:5, rep(5,5))
y=rep(1:5, 5)
pchs=c("!", "@", "#", "$", "%")
plot(1:5, type='n', xlim=c(0,7.5), ylim=c(0.5,5.5), main="points by ‘pch’ ")
points(x, y, pch=1:25, cex=2.5)
text(x-0.4, y, labels=as.character(1:25), cex=1.5)


plot(iris$Sepal.Width, iris$Sepal.Length, cex=1, pch=20, xlab="width", ylab="length", main="iris")
points(iris$Petal.Width, iris$Petal.Length, cex=1, pch="+", col="blue")
points(iris$Sepal.Width, iris$Sepal.Length, cex=1, pch=15, col="pink")


cars[1:4,]
z <- lm(dist ~ speed, data = cars)
is(z)
z$coef
plot(cars,main = "abline")

abline(h = 20)
abline(h = 30)
abline(v = 20, col="blue")
abline(a = 40, b = 4, col="red") # y = a + bx
abline(z, lty = 2, lwd = 2, col="green")



cars[1:10,]
z <- lm(dist ~ speed, data = cars)
is(z)
z$coef
plot(cars,main = "abline")
abline(h = 30)
abline(h = 50)
abline(v = 10, col='purple')
abline(a = 5, b = 5, col="red")
abline(z, lty=2, lwd=2, col="blue") ## reg인수
abline(z$coef, lty=3, lwd=2, col="orange") ## coef인수



lty1 = c('blank', 'solid', 'dashed', 'dotted', 'dotdash', 'longdash', 'twodash')
lty2 = c('33', '24', 'F2', '2F', '3313', 'F252', 'FF29')
plot(0:6, 0:6, type='n', ylim=c(0,20), xlab='', ylab='', main='lines')

lines(c(1,3), c(20,20), lty=1)
lines(c(1,3), c(19,19), lty=2)
lines(c(1,3), c(18,18), lty=3)
lines(c(1,3), c(17,17), lty=4)
lines(c(1,3), c(16,16), lty=5)
lines(c(1,3), c(15,15), lty=6)
lines(c(1,3), c(14,14), lty=lty1[1])
lines(c(1,3), c(13,13), lty=lty1[2])
lines(c(1,3), c(12,12), lty=lty1[3])
lines(c(1,3), c(11,11), lty=lty1[4])
lines(c(1,3), c(10,10), lty=lty1[5])
lines(c(1,3), c(9,9), lty=lty1[6])
lines(c(1,3), c(8,8), lty=lty1[7])
lines(c(1,3), c(7,7), lty=lty2[1])
lines(c(1,3), c(6,6), lty=lty2[2])
lines(c(1,3), c(5,5), lty=lty2[3])
lines(c(1,3), c(4,4), lty=lty2[4])
lines(c(1,3), c(3,3), lty=lty2[5])
lines(c(1,3), c(2,2), lty=lty2[6])
lines(c(1,3), c(1,1), lty=lty2[7])
legend(3.5, 20, legend=1:6, lty=1:6)
legend(3.5, 13, legend=c(lty1,lty2), lty=c(lty1,lty2))





plot(1:9, type='n', axes=F, xlab='', ylab='', main='arrows')
arrows(1, 9, 4, 9, angle=30, length=0.25, code=2)
arrows(1, 8, 4, 8, length=0.5)
arrows(1, 7, 4, 7, length=0.1)
arrows(1, 6, 4, 6, angle=60)
arrows(1, 5, 4, 5, angle=90)
arrows(1, 4, 4, 4, angle=120)
arrows(1, 3, 4, 3, code=0)
arrows(1, 2, 4, 2, code=1)
arrows(1, 1, 4, 1, code=3)


text(4.5, 9, adj=0, 'angle=30, length=0.25, code=2 (default)')
text(4.5, 8, adj=0, 'length=0.5')
text(4.5, 7, adj=0, 'length=0.1')
text(4.5, 6, adj=0, 'angle=60')
text(4.5, 5, adj=0, 'angle=90')
text(4.5, 4, adj=0, 'angle=120')
text(4.5, 3, adj=0, 'code=0')
text(4.5, 2, adj=0, 'code=1')
text(4.5, 1, adj=0, 'code=3')


op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
plot(1:10, type = "n", main = "rect", xlab = "", ylab = "", axes = F)
rect(xleft = 1, ybottom = 7, xright = 3, ytop = 9)
text(2, 9.5, adj = 0.5, "defalut")
rect(1, 4, 3, 6, col = "gold")
text(2, 6.5, adj = 0.5, "col = \"gold\"")
rect(1, 1, 3, 3, border = "gold")
text(2, 3.5, adj = 0.5, "border = \"gold\"")
rect(4, 7, 6, 9, density = 10)
text(5, 9.5, adj = 0.5, "density = 10")
rect(4, 4, 6, 6, density = 10, angle = 315)
text(5, 6.5, adj = 0.5, "density=10, angle=315")
rect(4, 1, 6, 3, density = 25)
text(5, 3.5, adj = 0.5, "density = 25")
rect(7, 7, 9, 9, lwd = 2)
text(8, 9.5, adj = 0.5, "lwd = 2")
rect(7, 4, 9, 6, lty = 2)
text(8, 6.5, adj = 0.5, "lty = 2")
rect(7, 1, 9, 3, lty = 2, density = 10)
text(8, 3.5, adj = 0.5, "lty=2, density=10")
par(op)



op <- par(no.readonly = TRUE)
par(mar = c(0, 2, 2, 2))
theta <- seq(-pi, pi, length = 12)
x <- cos(theta)
y <- sin(theta)
plot(1:6, type = "n", main = "PLOYGON", xlab = "", ylab = "", axes = F)
x1 <- x + 2
y1 <- y + 4.5

polygon(x1, y1)
x2 <- x + 2
y2 <- y + 2
polygon(x2, y2, col = "red", border="blue")
x3 <- x + 5
y3 <- y + 4.5
polygon(x3, y3, density = 10, angle=135)
x4 <- x + 5
y4 <- y + 2
polygon(x4, y4, lty = 2, lwd = 2)
text(2, 5.7, adj = 0.5, "defalut")
text(5, 5.7, adj = 0.5, "density = 10")
text(5, 3.2, adj = 0.5, "lty = 2, lwd = 2")
par(op)



plot(c(1, 8), c(-4, 4), type = "n")
x <- c(1, 2, 3, NA, 4, 4, 6, 6)
y <- c(1, -4, 3, NA, -3, 3, 3, -3)
polygon(x, y, col = c("pink", "blue"), border = c("red", "orange"), lwd = 2,
        lty = c("dotted", "solid"))
lines(c(1,8), c(-2,-2), lty=4, col="green")
arrows(1, 2, 8, 2, length=0.5)
title("Polygons") 