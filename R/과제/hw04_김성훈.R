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
colnames(data)[20] = '신용평점'

colSums(is.na(data))
for(i in 1:dim(data)[2]){
  data[is.na(data[,i]),i] = median(data[,i], na.rm = TRUE)
}

zero <- 0
one <- 0
for(i in 1:dim(data)[1]){
  ifelse(data$신용평점[i]<=5,zero <- zero + 1,one <-  one + 1)
}
data$신용평점 <- ifelse(data$신용평점<=5,0,1)
data$신용평점<-as.factor(data$신용평점)
data$신용평점

set.seed(123)
intrain<-createDataPartition(y=data$신용평점,p=0.63,list=FALSE)
intrain
training<-data[intrain,]## 트레이닝데이터
training
testing<-data[-intrain,]## 테스트 데이터 나눔
testing


##인공신경망 
set.seed(123)
m<-nnet(신용평점 ~ 유동비율 + 부채비율 + 총자산회전율 + 이자보상비율 + 단기차입금.총자본,
        size=3, #은닉층 노드 갯수
        linout=FALSE, # TRUE이면 활성함수가 선형출력(liner output) FALSE면 로지스틱함수가 적용
        skip = TRUE,
        MaxNWts=1000, # 가중치의 최대개수로 기본값은 1000, 모델이 복잡하다면 가중치의 수를 증가시켜야함.
        data=training)
#나머지 옵션도 있음. 찾아볼 것.
pre_nnet<-predict(m,newdata=testing)
head(pre_nnet)
pre_nnet<-as.factor(round(pre_nnet))
pre_nnet
#예측
confusionMatrix(pre_nnet,testing$신용평점)

# skip = TRUE
# 순이익증가율 특성 제거
# train, test 비율 0.7 -> 0.63
# 은닉층 노드 개수 5 -> 3
# 기존 정확도 0.85 -> 0.89 까지 상승