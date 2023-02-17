#1.
par(mfrow=c(3,1))
a <- sample(1:6,10, replace = T)
barplot(table(a), xlim=c(0,7), main='n=10')

a <- sample(1:6,1000, replace = T)
barplot(table(a), xlim=c(0,7), main='n=1000')

a <- sample(1:6,5000, replace = T)
barplot(table(a), xlim=c(0,7), main='n=5000')


#2. 이항분포관련 문제입니다. 아래 가지 조건 만족하는 분포도를 그리고 비교하여 설명해 주세요
plot(dbinom(x, 10, 0.5))
plot(dbinom(x, 10, 0.1))
plot(dbinom(x, 10, 0.9))

#3.
a <- pnorm(25000, mean=30000, sd=10000)
b <- pnorm(35000, mean=30000, sd=10000, lower.tail = FALSE)
1 - (a+b)
par(mfrow=c(1,1))
x <- seq(-10000, 70000, length=200)
plot(x, dnorm(x, mean=30000, sd=10000), type='l')
abline(v=25000,lty=2)
abline(v=35000,lty=2)
