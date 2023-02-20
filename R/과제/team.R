a = read.csv('data\\train.csv')
# 데이터 확인
str(a)
# 결측치 확인
sum(is.na(a))
# 필요없는 열 제거
b <- a[,c(-1,-2,-5,-7,-11)]
# 전체 데이터의 평균, 표준편차
mean(a['transaction_real_price'][,1])
sd(a['transaction_real_price'][,1])

# 도시별 실거래가의 boxplot
boxplot(transaction_real_price~city,data = a,ylim=c(0,400000))

# 도시별(서울, 부산)의 가격차이
# 영가설 : 차이없다
# 대립가설 : 서울이 부산보다 비싸다
# 각각의 평균, 표준편차를 구해 가설검정
seoul = b[b[1] == '서울특별시',]
busan = b[b[1] == '부산광역시',]

mean_busan <- mean(busan['transaction_real_price'][,1])
mean_seoul <- mean(seoul['transaction_real_price'][,1])
sd_busan <- sd(busan['transaction_real_price'][,1])
sd_seoul <- sd(seoul['transaction_real_price'][,1])

seoul_price <- c(nrow(seoul), mean_seoul, sd_seoul)
busan_price <- c(nrow(busan), mean_busan, sd_busan)

t <- function(x,y,a){
  t0 <- (x[2]-y[2])/sqrt((x[3]^2/x[1])+(y[3]^2/y[1]))
  if(t0>1.645){
    cat('영가설 기각')
  }else{
    cat('영가설 채택')
  }
}
t(seoul_price,busan_price,0.05)


# 같은 이름의 동끼리 다른 결과가 있나(ex-장충동1가,장충동2가)
# 영가설 : 같다
# 대립가설 : 같지 않다 (양측검정)
jang1 <- b[b$dong == '장충동1가',]
jang2 <- b[b$dong == '장충동2가',]
jang <- rbind(jang1,jang2)
boxplot(transaction_real_price~dong,data=jang)

mean_jang1 <- mean(jang1['transaction_real_price'][,1])
mean_jang2 <- mean(jang2['transaction_real_price'][,1])
sd_jang1 <- sd(jang1['transaction_real_price'][,1])
sd_jang2 <- sd(jang2['transaction_real_price'][,1])


jang1_price <- c(nrow(jang1), mean_jang1, sd_jang1)
jang2_price <- c(nrow(jang2), mean_jang2, sd_jang2)

t1 <- function(x,y,a){
  t0 <- (x[2]-y[2])/sqrt((x[3]^2/x[1])+(y[3]^2/y[1]))
  if(abs(t0)>2.58){
    cat('영가설 기각')
  }else{
    cat('영가설 채택')
  }
}
t1(jang1_price,jang2_price,0.01)


# 2000년 기준 이후 이전으로 가격차이
# 영가설 : 차이 없다
# 대립가설 : 2000년도가 더 비싸다
over_2000 <- b[b$year_of_completion>=2000,]
under_2000 <- b[b$year_of_completion<2000,]

over_2000$year_of_completion = 2000
under_2000$year_of_completion = 1980
year <- rbind(over_2000,under_2000)
boxplot(transaction_real_price~year_of_completion,data=year,ylim=c(0,300000))

mean_under <- mean(under_2000['transaction_real_price'][,1])
mean_over <- mean(over_2000['transaction_real_price'][,1])
sd_under <- sd(under_2000['transaction_real_price'][,1])
sd_over <- sd(over_2000['transaction_real_price'][,1])


over_price <- c(nrow(over_2000), mean_over, sd_over)
under_price <- c(nrow(under_2000), mean_under, sd_under)


t <- function(x,y,a){
  t0 <- (x[2]-y[2])/sqrt((x[3]^2/x[1])+(y[3]^2/y[1]))
  if(t0>2.33){
    cat('영가설 기각')
  }else{
    cat('영가설 채택')
  }
}
t(over_price,under_price,0.01)
