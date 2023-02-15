#1. R에서 데이터 자료형 분류
#-> 데이터 자료형의 특징, 저장 데이터 타입
#-> 자료형 변환 관련 함수들
#vector - 한가지 데이터 타입만 넣을 수 있는 1차원 자료형
#as.numeric()
#as.character()
#list - 여러가지 데이터 타입을 넣을 수 있는 1차원 자료형
#as.list()
#matrix - 한가지 데이터 타입을 넣을 수 있는 2차원 자료형
#as.matrix()
#data.frame - 여러가지 데이터 타입을 넣을 수 있는 2차원 자료형
#as.data.frame()

#-------------------------------------------------------------
#2. 메타데이터란?
#  -> 개념
#데이터를 설명 해주는 데이터

#-------------------------------------------------------------
#3. 기술적통계 방식으로 데이터 표현
#-> 데이터 :  사회일반 > 가족실태조사 > 총괄(제공) > 2020
#-> 추출 데이터 : 지역, 가족원합계, 세대구성, 가구구성, 교육정도_학력
family <- read.csv('가구.csv',header=F)
colnames(family)[1] = '지역'
colnames(family)[2] = '가족원합계'
colnames(family)[3] = '세대구성'
colnames(family)[4] = '가구구성'
colnames(family)[5] = '학력'

family$지역 <- factor(family$지역, levels = c(11,21:26,29,31:39), labels=c('서울특별시','부산광역시','대구광역시',
                                                                       '인천광역시','광주광역시','대전광역시',
                                                                       '울산광역시','세종특별자치시','경기도',
                                                                       '강원도','충청북도','충청남도','전라북도',
                                                                       '전라남도','경상북도','경상남도','제주특별자치도'))

family$세대구성 <- factor(family$세대구성, levels = 1:6, labels=c('1세대','2세대','3세대',
                                                      '4세대','1인 가구','비혈연'))

#family$가구구성 <- factor(family$가구구성, levels = 1:26, labels=c('미혼여성','미혼남성','기혼여성','기혼남성','여성노인',
                                                       '남성노인','부부','부부 + 자녀','모 + 자녀','부 + 자녀',
                                                       '모 + 자녀부부','부 + 자녀부부','부모 + 자녀부부','부모 + 자녀부부 + 손자녀',
                                                       '부모 + 모 + 손자녀','부모 + 부 + 손자녀','모 + 자녀부부 + 손자녀',
                                                       '부 + 자녀부부 + 손자녀','모친 + 모 + 손자녀','모친 + 부 + 손자녀','부친 + 부 + 손자녀',
                                                       '부친 + 모 + 손자녀','조부모 + 손자녀','조모 + 손자녀','조부 + 손자녀','기타'))

family$학력 <- factor(family$학력, levels = 0:6, labels=c('안받았음','초등학교','중학교',
                                                      '고등학교','대학교(4년제 미만)','대학교(4년제 이상)',
                                                      '대학원'))
#(3-1) 지역
#- 지역별 세대구성 비중, 가구구성 비중
#- 가장 많은 세대구성, 가구구성,  가장 적은 세대구성, 가구구성,  평균 세대구성, 가구구성
table(family$지역,family$가구구성)
max(table(family$세대구성))
max(table(family$가구구성))
min(table(family$세대구성))
min(table(family$가구구성))
mean(table(family$세대구성))
mean(table(family$가구구성))

#(3-2) 가족원합계
#- 전체에 대한 비중으로 표현
#- 가장 많은 가족원 수, 가장 적은 가족원 수, 평균 가족원 수 
pie(table(family$가족원합계))

cnt <- 0
for(i in 1:11){
  if(table(family$가족원합계)[i] == max(table(family$가족원합계))){
    cat('가장 많은 가족원 수',i,'명\n')
  }else if(table(family$가족원합계)[i] == min(table(family$가족원합계))){
    cat('가장 적은 가족원 수',i,'명')
  }
  if(i == 11){
    cnt = cnt + (12 * table(family$가족원합계)[i])
  }else{
    cnt = cnt + (i * table(family$가족원합계)[i])
  }
  
}
cnt / sum(table(family$가족원합계))


#(3-3) 세대구성
#- 세대구성별 수
#- 1인가구 수와 나머지 세대구성 수 비교
barplot(table(family$세대구성))
one_person <- table(family$세대구성)[5]
other <- sum(table(family$세대구성))-one_person
names(other) = '나머지'
pie(cbind(other,one_person),labels=c('나머지','1인 가구'))

#(3-4) 가구구성과 교육정도_학력
#- 가족구성와 학력의 관계
plot(family$학력,family$가구구성)
