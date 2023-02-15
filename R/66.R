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
