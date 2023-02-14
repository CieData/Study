#---------------------------------------------------
# 내장 데이터 cars 활용
# cars 데이터 정보 출력
# 50대 자동차의 속도와 제동거리 관계 그래프화
#---------------------------------------------------
# 데이터 로딩
cars
# 데이터 확인
# (1) 데이터 요약 정보 & 구조 출력
str(cars)

# (2) 행과 열 출력
dim(cars)

# (3-1) 행 갯수만 출력
nrow(cars)

# (3-2) 열 갯수만 출력
ncol(cars)

# (4) 컬럼명 출력
colnames(cars)

# 데이터 표현 By 산점도 그래프
plot(cars$speed, cars$dist, main = '속도별 거리', xlab = '속도', ylab = '거리')


str(Nile)
plot(Nile)

# -----------------------------------------------
# 이산적 데이터 자료를 표현
# -> 각 데이터(값)에 빈도를 표현 >> table()
# -> 막대 그래프 표현
# -----------------------------------------------
# 외부 데이터 로딩

raw_data = read.csv('인구조사.csv',header=F)
str(raw_data)

# 데이터 백업 => save(데이터, 파일경로)
savePath = '인구조사.Rdata'
save(raw_data, file = savePath)

# 코드(숫자 자료형) 범주형 데이터를 문자형으로 변환
# factor(데이터, levels, labels)
raw_data$V1 <- factor(raw_data$V1, levels = 1:2, labels=c('남자','여자'))
unique(raw_data$V6)

mode(table(raw_data$V3))

barplot(table(raw_data$V5))

