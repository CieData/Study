cafeData <- read.csv('data\\cafedata.csv')
str(cafeData)

sum(is.na(cafeData))
sum(is.na(cafeData$Coffees))
# na.omit()결측치 삭제
cafeData <- na.omit(cafeData)

# 행단위 NA검사 >> 행의 모든 요소가 NA가 아니어야 TRUE
complete.cases(cafeData)

# 최빈값
y <- table(cafeData$Coffees)
names(which(y == max(y)))

# 줄기잎 그래프
data <- c(1,1,2,2,3,3,3,3,4)
stem(data)

data <- c(1,11,11,22,22,23,31,32,33,34,40)
stem(data)



# 표준편차

height <- c(164,166,168,170,172,174,176)
#(1) 평균
height.m <- mean(height)
#(2) 편차
s <- height-height.m
#(3) 분산
v <- sum(s**2)/(length(height)-1)
v1 <- mean(s**2)
c(v,v1)
#표준편차
sqrt(v)

var(height)
sd(height)



# 실습
airquality
nrow(airquality) - sum(complete.cases(airquality))
data <- na.omit(airquality)

for(i in 1:6){
  cat(names(data[i]),'\n')
  cat(mean(data[[i]]),'\n')
  cat(var(data[[i]]),'\n')
  cat(sd(data[[i]]),'\n')
  y <- table(data[i])
  cat(names(which(y == max(y))),'\n\n')
}


## iris
# 데이터 기본 정보 출력
str(iris)

# 결측치 체크 & 처리
sum(is.na(iris))

# 꽃받침 너비에 대한 이상치 체크
boxplot.stats(iris$Sepal.Width)$out

summary(iris)[2,]
quantile(iris$Sepal.Width)
